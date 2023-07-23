from pathlib import Path
import csv

# ## we can use this to inspect/check what is cwd:
# print(Path.cwd())

# ## setup filepaths for reading the Cash_on_Hand.csv:
fp = Path.cwd()/"CSV_Reports"/"Cash_on_Hand.csv"
fp_write = Path.cwd()/"summary_report.txt"

def coh_function():
        with fp.open(mode="r",encoding="UTF-8", newline="") as file:
            reader = csv.reader(file)
            ## skip the first row which is the header of the values
            next(reader)

            # created an empty list to input data in it
            coh_list = []

            ## for loop is used append the data of the day and cash on hand values 
            ## in each row into the empty list
            for row in reader:
                coh_list.append([int(row[0]),int(row[1])])

        ## a variable is assigned to a range from 0 to 90
        ## to represent the total number of days of the csv
        number_of_days = range(0,90)
        ## empty list is created to accumulate and assign all the surplus value
        surplus = []

        ## "for loop" is used to repeat the code according to the range given
        ## in this case 90.
        with fp_write.open(mode="a", encoding="UTF8", newline="") as file:
            for num in number_of_days:

                ## a variable "diff" is assigned to a formula
                ## to calculate the difference between the value of cash on hand
                ## between the day after and the current day
                diff = coh_list[num + 1][1] - coh_list[num][1]

            ## Use of "if" condiiton
            ## If the difference in cash is more 0
            ## it is a cash surplus which would be
            ## appended to the surplus list
                if diff > 0:
                    surplus.append(diff)
                
                ## If the difference calculated  for the day is less than zero,
                ## it is a cash deficit.
                ## The day and the amount of deficit will then be printed in a statement 
                ## for each day cash deficit occurs.
                elif diff < 0:
                    file.write(f"\n[CASH DEFICIT] DAY: {num + 1}, AMOUNT: USD{diff * -1}")
                    print(f"[CASH DEFICIT] DAY: {num + 1}, AMOUNT: USD{diff * -1}")
                
            ## Use of "if" condition
            ## If the length of surplus list is equal
            ## to the number of days(90), the statement would be printed
                if len(surplus) == 90:  
                    file.write(f"\n[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
                    print(f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
            ## set of codes under the if condition will run if there are values in the surplus variable
                    if surplus:
            ## max() is used to find the highest amount in the surplus list
                        max_surplus = max(surplus)
                        # use enumerate to include a counter for each loop
                        for count, num in enumerate(surplus):
                            # loop will stop once value of surplus is the highest
                            if num == max_surplus:
                                break
        
            ## Statement is printed to show the day with the highest cash surplus
            ## as well as the amount of cash surplus
                        file.write(f"\n[HIGHEST CASH SURPLUS] DAY: {count + 1}, AMOUNT: USD{max(surplus)}")
                        print(f"[HIGHEST CASH SURPLUS] DAY: {count + 1}, AMOUNT: USD{max(surplus)}")
                
                    

