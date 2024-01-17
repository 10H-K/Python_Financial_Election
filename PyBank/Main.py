#Import os Module
import os

#Import Module For CSV Files
import csv

#Import Module For Date/Time Manipulation
from datetime import datetime

#Import Module For Mean Determination
from statistics import mean

#File Path To Target CSV File (PyBank Financial Dataset)
pybank_csvpath = os.path.join("Resources", "budget_data.csv")

#Store CSV File Data & Data From Further Manipulation
months = [] #Months From Date Column In CSV File
years = set() #Calendar Year From Date Column In CSV File
date_column = [] #Data Directly From Date Column In CSV File
profit_losses_column = [] #Data Directly From Profit/Losses Column In CSV File
profit_losses_changes = [] #Changes In Profit/Losses On A Monthly Basis

#Variables For Monthly Profit/Losses Change Analysis
profit_losses_changes_maximum = 0
profit_losses_changes_maximum_date = " "
profit_losses_changes_minimum = 0
profit_losses_changes_minimum_date = " "

#Open budget_data CSV File Through Variable pybank_csvpath
with open(pybank_csvpath) as pybank_csvfile:

    #Create CSV Reader Object Using CSV Module
    pybank_csvreader = csv.reader(pybank_csvfile, delimiter=',')

    #Read CSV File Header Row First, Store As Variable Then Skip
    pybank_csv_header = next(pybank_csvreader)

    #Read All Rows Following Header
    for row in pybank_csvreader:
        
        #Extract/Store Data From Date Column & Profit/Losses Column
        date_column_values = row[0]
        date_column.append(date_column_values)
        profit_losses_column_values = row[1]
        profit_losses_column.append(int(profit_losses_column_values))

        #Convert Date Column To DateTime Object
        date_object = datetime.strptime(date_column_values, "%b-%y")
        months.append(date_object.strftime("%b")) #Extract Month And Append To Months List
        years.add(date_object.year) #Extract Year And Append To Years Set 

    #Convert years To List Of Unique Strings, Sorted In Ascending Order
    years = sorted(map(str, years))

    #Convert years List To Single List With All Unique Calendar Years
    years_string = ', '.join(years)

    #Net Total Amount Of Profit/Losses
    profit_losses_net_total = sum(profit_losses_column)

    #Monthly Changes In Profit/Losses
    profit_losses_changes = [profit_losses_column[i] - profit_losses_column[i-1] for i in range(1, len(profit_losses_column))]

    #Average Of Monthly Changes In Profit/Losses
    profit_losses_changes_average = mean(profit_losses_changes)

    #Maximum & Minimum Of Monthly Changes In Profit/Losses
    profit_losses_changes_maximum = max(profit_losses_changes)
    profit_losses_changes_minimum = min(profit_losses_changes)

    #Dates For Maximum & Minimum Of Monthly Changes in Profit/Losses
    profit_losses_changes_maximum_list_position = profit_losses_changes.index(max(profit_losses_changes))
    profit_losses_changes_minimum_list_position = profit_losses_changes.index(min(profit_losses_changes))
    profit_losses_changes_maximum_date = date_column[profit_losses_changes_maximum_list_position+1]
    profit_losses_changes_minimum_date = date_column[profit_losses_changes_minimum_list_position+1]

#Print Statements For Results Display In Terminal
print("\nFinancial Analysis")
print(" ")
print("----------------------------")
print(" ")
print("Total Months:", len(months))
print(" ")
print("Years Associated with Financial Data:", years_string)
print(" ")
print("----------------------------")
print(" ")
print("Net Total of Profit/Losses:", "${:,}".format(profit_losses_net_total))
print(" ")
print("Average Monthly Change in Profit/Losses:", "${:,.2f}".format(profit_losses_changes_average))
print(" ")
print("----------------------------")
print(" ")
print("Greatest Increase in Profits:", profit_losses_changes_maximum_date + " (${:,}".format(profit_losses_changes_maximum) + ")")
print(" ")
print("Greatest Decrease in Profits:", profit_losses_changes_minimum_date + " (${:,}".format(profit_losses_changes_minimum) + ")")
print(" ")
print("----------------------------")

#Specify Location & Create Text File Containing Same Results
PyBank_Results_path = os.path.join("Analysis", "PyBank_Results.txt")

#Write Text File To Input Results
with open(PyBank_Results_path, 'w') as output_file:
    print("Financial Analysis", file=output_file)
    print(" ", file=output_file)
    print("----------------------------", file=output_file)
    print(" ", file=output_file)
    print("Total Months:", len(months), file=output_file)
    print(" ", file=output_file)
    print("Years Associated with Financial Data:", years_string, file=output_file)
    print(" ", file=output_file)
    print("----------------------------", file=output_file)
    print(" ", file=output_file)
    print("Net Total of Profit/Losses:", "${:,}".format(profit_losses_net_total), file=output_file)
    print(" ", file=output_file)
    print("Average Monthly Change in Profit/Losses:", "${:,.2f}".format(profit_losses_changes_average), file=output_file)
    print(" ", file=output_file)
    print("----------------------------", file=output_file)
    print(" ", file=output_file)
    print("Greatest Increase in Profits:", profit_losses_changes_maximum_date + " (${:,}".format(profit_losses_changes_maximum) + ")", file=output_file)
    print(" ", file=output_file)
    print("Greatest Decrease in Profits:", profit_losses_changes_minimum_date + " (${:,}".format(profit_losses_changes_minimum) + ")", file=output_file)
    print(" ", file=output_file)
    print("----------------------------", file=output_file)
