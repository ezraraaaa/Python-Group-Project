from pathlib import Path
import csv

# create a file to csv file.
fp =Path.cwd()/"CSV_Reports"/"Cash_on_Hand.csv"

def overheads_func():
        
    largest = 0
    name = ''
    # read the csv file to append profit and quantity from the csv.
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        
        #skip the header row in the csv file 
        next(reader) 
    
    #iterate each row in the csv file
        for row in reader:
            #check if the profit in the current row is larger than the current largest overhead
            if float(row[1]) >= largest:
                #update the largest overhead and its corresponding name
                largest = float(row[1])
                name = row[0]
                
    #print highest overhead and its corresponding name
    print (f"[HIGHEST OVERHEAD] {name}: {largest}%")
