## import required modules
from pathlib import Path
import csv

# ## we can use this to inspect/check what is cwd:
# print(Path.cwd())

# ## setup filepaths for reading:
fp_read = Path.cwd()/"CSV_Reports"/"Profits_and_Loss.csv"

def profitloss_function():
    fp_read = Path.cwd()/"CSV_Reports"/"Profits_and_Loss.csv"
    fp_write = Path.cwd()/"summary_report.txt"
    fp_write.touch()

    with fp_read.open(mode="r", encoding="UTF8", newline="") as file:
        
        reader = csv.reader(file) # create csv reader object using csv
        
        next(reader)              # to skip reading header
        
        profitsLoss = []         # create empty list

        for row in reader:        # iterate each row with loop
            # print(row)            # just to inspect, can remove later
            
            # appending list of current row into list
            profitsLoss.append([int(row[0]), int(row[1]), int(row[2]), int(row[3]), int(row[4])])


    # initialization of profitCount variable
    profitCount = 0
    # initialization of bestProfit variable
    bestProfit = 0

    # opening the file to append
    with fp_write.open(mode="a", encoding="UTF8", newline="") as file:
        
        # for loop for the length of the list
        for i in range(len(profitsLoss)):
        
            # skip if its the first day
            if i != 0:
            
                # previous day's profit
                prevProfit = profitsLoss[i - 1][4]
                # today's profit
                currProfit = profitsLoss[i][4]
                # print("DAY: " + str(profitsLoss[i][0]))   # printing the day, testing
                # print(prevProfit, currProfit)             # printing previous and current profit, testing
            
                # if today's profit is less than previous day's profit
                if currProfit < prevProfit:
                    # calculate the difference
                    difference = prevProfit - currProfit
                    # printing & appending of deficit into the output file
                    file.write(f"[PROFIT DEFICIT] DAY: " + str(profitsLoss[i][0]) + ", AMOUNT: USD" + str(difference))
                    print("[PROFIT DEFICIT] DAY: " + str(profitsLoss[i][0]) + ", AMOUNT: USD" + str(difference))
                
                # else if current profit is more than previous profit
                elif currProfit > prevProfit:
                    # increase profitCount
                    profitCount+=1

                    # if the current profit surplus is bigger than the previous bestProfit,
                    if currProfit - prevProfit > bestProfit:
                        # replace the existing bestProfit
                        bestProfit = currProfit - prevProfit
                        # saving the day of the best profit
                        bestProfitDay = profitsLoss[i][0]
                    
                # else if the profitCount is the length of the list - 1, meaning that it has profited everyday, skipping day 1.
                elif profitCount == len(profitsLoss) - 1:
                
                    # print & append the net profit surplus, and the best profit surplus into the output file
                    file.write(f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n[HIGHEST NET PROFIT SURPLUS] DAY: " + str(bestProfitDay) + ", AMOUNT: " + str(bestProfit))
                    print("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n[HIGHEST NET PROFIT SURPLUS] DAY: " + str(bestProfitDay) + ", AMOUNT: " + str(bestProfit))