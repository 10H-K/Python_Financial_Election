# Utilizing Python for Financial Analysis (PyBank) and Election Results (PyPoll)


## Overview ##

The objective of this project is to create two separate Python scripts. The first Python script will assess the financial dataset of a company, which is organized as an Excel sheet with two columns (Date, Profit/Losses). This Python script will analyze the financial dataset and output the following values: total number of months in dataset, net total for Profit/Losses, monthly changes in Profit/Losses, average of monthly changes in Profit/Losses, date corresponding to greatest increase in profits, and date corresponding to greatest decrease in profits. The second Python script will assess a set of poll data from Colorado, which is organized as an Excel sheet with three columns (Voter ID, County, Candidate). The Python script will analyze the poll data and output the following values: total number of votes cast, counties that participated in the election, complete list of candidates that received votes, percentage of votes won by each candidate, total number of votes won by each candidate, and winner of the election based on popular vote. The application of Python to both situations demonstrates the usefulness of Python scripting skills.


## Process ##

A) PyBank Python script basic structure:
  1. Importation of necessary modules (os, csv, datetime, statistics)
  2. Establishment of file path to target CSV file ("budget_data.csv")
  3. Creation of:
      * empty lists for direct storage of CSV file data (Date & Profit/Losses columns)
      * empty lists for storage of months and monthly changes in profit/losses
      * empty set for storage of unique calendar years
  4. Creation and initialization of variables for analysis of monthly changes in profit/losses
  5. Usage of CSV module to open and read target CSV file ("budget_data.csv")
  6. Storage of CSV file header row as variable then skipping header row
  7. Iteration through rows following header row using For Loop
      * extraction and storage of data from date column & profit/losses column
      * conversion of date column to DateTime object and extraction/storage of months and years
  8. Conversion of years set to list of strings, sorted in ascending order
  9. Conversion of years list to a single list containing all calendar years separated by commas
  10. Determination of net total amount of profit/losses
  11. Determination of changes in profit/losses on a monthly basis
  12. Determination of average of monthly changes in profit/losses
  13. Determination of maximum & minimum monthly changes in profit/losses
  14. Determination of dates corresponding to maximum & minimum monthly changes in profit/losses
  15. Statements with results printed to terminal
  16. Specification of location & creation of new text file containing same results
  17. Statements with results printed to newly created text file


B) PyPoll Python script basic structure:
  1. Importation of necessary modules (os, csv)
  2. Establishment of file path to target CSV file ("election_data.csv")
  3. Creation of empty lists for direct storage of CSV file data (Ballot ID/County/Candidate columns)
  4. Usage of CSV module to open and read target CSV file ("election_data.csv")
  5. Storage of CSV file header row as variable then skipping header row
  6. Iteration through rows following header row using For Loop
      * extraction and storage of data directly from Ballot ID/County/Candidate columns
  7. Usage of set and sort functions to create lists of unique candidates/counties in alphabetical order
  8. Creation of two dictionaries:
      * First dictionary to store running vote tally for each individual candidate
      * Second empty dictionary to store votes received percentages for each individual candidate 
  9. Iteration through list containing all voter candidate choices using For Loop
      * primary goal of updating running vote tallies
  10. Determination of total number of votes cast
  11. Specification of location & creation of new text file containing same results
  12. Statements with total votes and participating counties printed to terminal and text file
  13. Calculation of votes received percentages
  14. Statements with results for individual candidates printed to terminal and text file
  15. Determination of election winner
  16. Statement with election winner printed to terminal and text file


## Results PyBank ##

![image](https://github.com/10H-K/Python_Financial_Election/assets/152930492/2ba090f3-9742-47e9-b5f0-bc1d81c44bcf)

![image](https://github.com/10H-K/Python_Financial_Election/assets/152930492/fac5e6de-8259-4bca-b848-26d6d1adff9b)


## Results PyPoll ##

![image](https://github.com/10H-K/Python_Financial_Election/assets/152930492/5bf4f072-e590-424b-b8ee-a32c8666278f)

![image](https://github.com/10H-K/Python_Financial_Election/assets/152930492/70a1e93c-8bdf-46cc-b779-ef315ae2ff3d)
