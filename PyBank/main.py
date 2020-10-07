import os
import csv
csvpath = os.path.join("Resources", "budget_data.csv")
Date=[]
Budget=[]
TotalChanges=[]
Average=[]

# Open and read csv
with open(csvpath) as csv_file:
    csvreader =csv.reader(csv_file, delimiter=",")
 

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvreader)
    #print(csvreader)
    #print(f"Header: {csv_header}")

    #Read each row of data after the header
    #cont=0
    for row in csvreader:
        #cont no necessary  with len 
        #cont+=1
        Date.append(row[0])
        #Budget.append(row[1]) #se sustituye por el int  ****
        Budget.append(int(row[1])) #insert Total Budget
    
    #values totals change per month 
    for i in range(len(Budget)-1):
        #TotalChanges=(Budget.append(int(row[1]+1)))-(Budget.append(int(row[1])))
        TotalChanges.append(Budget[i+1]-Budget[i])
        #Average
        #Average.append(sum(TotalChanges)/len(TotalChanges))
    
    
        MaxGreatestIncrease= max(TotalChanges)
        MonthIncrease = Date[TotalChanges.index(MaxGreatestIncrease)+1]
        #print(MaxGreatestIncrease)
        #print(MonthIncrease)

        MinGreatestDecrease=min(TotalChanges)
        MonthDecrease = Date[TotalChanges.index(MinGreatestDecrease)+1]
        #print(MinGreatestDecrease)        
        #print(MonthDecrease)
        

    
print(f"Financial Analysis")
print(f"----------------------------------------")
print(f"Total Months:{len(Budget)}")
print(f"Total:${sum(Budget)}")
print(f"Average Change:${round(sum(TotalChanges)/len(TotalChanges),2)}")
print(f"Greatest Increase in Profits: {(MonthIncrease)} (${MaxGreatestIncrease})")
print(f"Greatest Decrease in Profits: {(MonthDecrease)} (${MinGreatestDecrease})")


# Specify the file to write to
output_path = os.path.join("analysis", "Financial Analysis.txt")
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path,'w') as outfile:

    # Initialize csv.writer
    #csvwriter = csv.writer(outfile)
    #Write the first row (column headers)
    #csvwriter.writerow("Financial Analysis")
    
    outfile.write("Financial Analysis\n")
    outfile.write("------------------------------------------------\n")
    outfile.write(f"Total Months: {len(Budget)}\n")
    outfile.write(f"Total:${sum(Budget)}\n")
    outfile.write(f"Average Change:${round(sum(TotalChanges)/len(TotalChanges),2)}\n")
    outfile.write(f"Greatest Increase in Profits: {(MonthIncrease)} (${MaxGreatestIncrease}) \n")
    outfile.write(f"Greatest Decrease in Profits: {(MonthDecrease)} (${MinGreatestDecrease}) \n")

   


