#!/bin/bash

#Modify the arguments below to run the script
#--URL: Enter the USCIS webpage URL
#--RECEIPT_NUMBER: Enter your receipt number or case number (they're the same)
#--RANGE: Enter the range to which you want to scan other receipt numbers around yours
#--FILE_PATH: Enter the file name (or path) for the .csv report
python main.py --URL "https://egov.uscis.gov/casestatus/landing.do" --RECEIPT_NUMBER "YSC2190032700" --RANGE 10  --FILE_PATH "scan_100.csv"  

