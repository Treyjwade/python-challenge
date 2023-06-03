# import modules
import os
import csv
# csv path
#csvpath = os.path.join('Resources', 'budget_data.csv')
csvpath="Resources/budget_data.csv"
# csv reader
# csvreader = csv.reader(budget_data.csv, delimiter=',')
# Variables for total months
total_months = 0 
# variable for total profit and loss
totalp_l = 0
change_list =[]
month_of_change=[]
greatest_increase=["", 0]
greatest_decrease=["",9999999999]

with open(csvpath,'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    header = next(csv_reader)
    first_row = next(csv_reader)
    total_months += 1 
    change = float(first_row[1])
    totalp_l += change 
    for row in csv_reader:
        #print(row)
        total_months += 1 
        #change = float(row[1])
        totalp_l += float(row[1])
        net_change = float(row[1]) - change
        change =float(row[1])
        #change_list.append(change)
        change_list += [net_change]
        month_of_change += [row[0]]

        if net_change > greatest_increase[1]:
            greatest_increase[1]= net_change
            greatest_increase[0]= row[0]

        if net_change < greatest_decrease[1]:
            greatest_decrease[1]= net_change
            greatest_decrease[0]= row[0]

average = sum(change_list)/len(change_list)

result= f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${totalp_l}
Average Change: ${average:.2f}
Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})
Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})


"""
print(result)
outputpath = "Analysis/budgetAnalysis.txt"
with open (outputpath,'w') as txt:
    txt.write(result)