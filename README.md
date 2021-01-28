# Ratchet_EAD_Tracker
A very basic script to extract the USCIS website for EAD case status updates. At this moment, all it does is take a given receipt number and scan statuses for a range of recept numbers around it. The output report will be provided in .csv. 

## Script Arguments

Below are the inputs that the script is expecting:
- URL: Enter the USCIS webpage URL
- RECEIPT_NUMBER: Enter your receipt number or case number (they're the same)
- RANGE: Enter the range to which you want to scan other receipt numbers around yours
- FILE_PATH: Enter the file name (or path) for the .csv reports


## Chrome Driver Installation
Before you're able to run this, you need to install Chrome Driver.
Below is the line to install this for Mac OS in terminal:
```bash
brew install chromedriver
```
If you use windows, you could probably look it up.

## Running the Script
### with environment
If you dont want the hastle of installing packages, I have provided a script that runs the entire script with the packages managed within it (see [run_env_script.sh](https://github.com/kmanchel/Ratchet_EAD_Tracker/blob/main/run_env_script.sh). This requires conda. If you don't have it, follow their installation instructions [here](https://docs.conda.io/projects/conda/en/4.6.1/user-guide/install/macos.html).
After updating the script arguments, run this on your terminal:
```bash
sh run_env_script.sh
```
### using your own environment
If you would like too manually set up your python env, check [requirements.txt](https://github.com/kmanchel/Ratchet_EAD_Tracker/blob/main/requirements.txt) and install those using pip. 
After updating the script arguments, run this on your terminal:
```bash
sh run_script_only.sh
```


**Note: There may be some cosmetic bugs in the text parsing, but I won't provide support on those fixes.**
