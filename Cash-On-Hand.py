## import required modules
from pathlib import Path
import csv

# ## we can use this to inspect/check what is cwd:
# print(Path.cwd())

# ## setup filepaths for reading:
fp_read = Path.cwd()/"CSV_Reports"/"Cash_on_Hand.csv"

def coh_function():
    fp_read = Path.cwd()/"CSV_Reports"/"Cash_on_Hand.csv"

    diff_list= []

    with fp_read.open(mode="r", encoding="UTF8", newline="") as file:
        reader = csv.reader(file) # create csv reader object using csv
        next(reader)              # to skip reading header
        for row in reader:        # iterate each row with loop
            # print(row)            # just to inspect, can remove later
            diff_list.append(float(row[2]))

        # print(cp_list)  # just to check, can remove later

        # Calculate average closing price
        avg_cp = sum(cp_list)/len(cp_list)

