# Imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from tqdm import tqdm
import time
import pandas as pd
import argparse

# Extract Function
def extract(URL, RECEIPT_NUMBER, quit=False):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    web = webdriver.Chrome(chrome_options=chrome_options)
    web.get(URL)

    # time.sleep(1)

    receipt_num = web.find_element_by_xpath('//*[@id="receipt_number"]')
    receipt_num.send_keys(RECEIPT_NUMBER)

    Check = web.find_element_by_xpath(
        '//*[@id="landingForm"]/div/div[1]/div/div[1]/fieldset/div[2]/div[2]/input'
    )
    Check.click()

    # time.sleep(1)
    try:
        status = web.find_element_by_xpath(
            "/html/body/div[2]/form/div/div[1]/div/div/div[2]/div[3]/h1"
        ).text

        received_date = web.find_element_by_xpath(
            "/html/body/div[2]/form/div/div[1]/div/div/div[2]/div[3]/p"
        ).text
        received_date = received_date[3 : received_date.find(", 2020")]
        if len(received_date) > 40:
            received_date = received_date[0 : received_date.find(", 2021")]
    except:
        status = "INVALID"
        received_date = "INVALID"

    web.close()
    if quit:
        web.quit()

    return status, received_date


# Main Function


def scan_range(URL, RECEIPT_NUMBER, RANGE, file_path):
    Receipt_Nos = []
    Status = []
    Receipt_Dates = []
    if (RANGE != 10) and (RANGE != 100) and (RANGE != 1000):
        raise ValueError(
            "You entered RANGE={}. Enter one of the following ranges: 10, 100, 1000".format(RANGE)
        )
        return
    size = len(str(RANGE)) - 1
    receipt_start = RECEIPT_NUMBER[:-size]
    to_quit = False

    print("SCANNING {} RANGE FROM {}...".format(RANGE, receipt_start))
    print("_______________________________________________")
    for i in tqdm(range(0, RANGE), "Scanning Range"):
        if RANGE == 10:
            receipt_end = "{0:0=1d}".format(i)
        elif RANGE == 100:
            receipt_end = "{0:0=2d}".format(i)
        else:
            receipt_end = "{0:0=3d}".format(i)
        receipt_no = receipt_start + receipt_end
        if i == RANGE - 1:
            to_quit = True
        current_status, receipt_date = extract(URL, receipt_no, to_quit)
        print("***********************************")
        print("RECEIPT NUMBER: {}".format(receipt_no))
        print("CURRENT STATUS: {} | UPDATED ON: {}".format(current_status, receipt_date))
        print("***********************************")

        Receipt_Nos.append(receipt_no)
        Status.append(current_status)
        Receipt_Dates.append(receipt_date)

    data = {
        "Receipt Numbers": Receipt_Nos,
        "Current Status": Status,
        "Status Updated": Receipt_Dates,
    }
    df = pd.DataFrame(data)

    df.to_csv(file_path, index=False)
    print("SCAN COMPLETEE")
    print("File written to {}".format(file_path))
    print("_______________________________________________")

    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--URL", type=str, required=True, help="Enter the USCIS URL")
    parser.add_argument(
        "--RECEIPT_NUMBER", type=str, required=True, help="Enter your receipt/case number"
    )
    parser.add_argument(
        "--RANGE",
        type=int,
        required=True,
        help="Enter range to scan other receipt numbers near yours",
    )
    parser.add_argument("--FILE_PATH", type=str, required=True, help="Path for saving report .csv")

    args = parser.parse_args()
    URL = args.URL
    RECEIPT_NUMBER = args.RECEIPT_NUMBER
    RANGE = args.RANGE
    file_path = args.FILE_PATH

    current_status, receipt_date = extract(URL, RECEIPT_NUMBER)
    print("***********************************")
    print("RECEIPT NUMBER: {}".format(RECEIPT_NUMBER))
    print("CURRENT STATUS: {} | UPDATED ON: {}".format(current_status, receipt_date))
    print("***********************************")

    scan_range(URL, RECEIPT_NUMBER, RANGE, file_path)
