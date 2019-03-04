import os
import csv

PyBankcsv = '/Users/vanjoisscott/Desktop/python-challenge/budget_data.csv'

Total_Months = 0
Total_Revenue = 0
Average_Change = 0
Total_Change = 0
RevenueInc = 0
Previous = 0
Average_Change = 0
greatestIncProfit = 0
greatestDecProfit = 0


        
with open(PyBankcsv, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    for m in csvreader:
        Total_Revenue = Total_Revenue + float(m[1])
        #Count the total of months
        #Total_Months = len(list(csvreader))
        Total_Months = Total_Months + 1
    
        
        RevenueInc = float(m[1]) - Previous
        Previous = float(m[1])
        Total_Change = Total_Change + RevenueInc
        #Calc Average Change
        Average_Change = round(Total_Change/Total_Months,2)
        
        if(RevenueInc > greatestIncProfit):
            greatestIncDate = m[0] 
            greatestIncProfit = RevenueInc
             
         
        if(RevenueInc < greatestDecProfit):
            greatestDate = m[0]
            greatestDecProfit = RevenueInc
               
                
print("Financial Analysis")
print("----------------------------")
print("Total Months: "+str(Total_Months))
print("Total Revenue: $" + str(Total_Revenue))
print("Average Revenue Change: $"+str(Average_Change))
print("Greatest Increase in Revenue: "+greatestIncDate + " ($" + str(greatestIncProfit) +")")
print("Greatest Decrease in Revenue: "+greatestDate + " ($" + str(greatestDecProfit) +")")

f = open("PyBank.txt", "w")
f.write("Financial Analysis"+ "\n")
f.write("_________________________"+ "\n")
f.write("Total Months: " + str(Total_Months)+"\n")
f.write("Total Revenue: $" + str(Total_Revenue)+ "\n")
f.write("Average Revenue Change: $" + str(Average_Change)+"\n")
f.write("Greatest Increase in Revenue:  "+greatestIncDate + " ($" + str(greatestIncProfit) +"\n")
f.write("Greatest Decrease in Revenue: "+greatestDate + " ($" + str(greatestDecProfit)+"\n")

f.close()