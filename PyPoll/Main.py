#Import os Module
import os

#Import Module For CSV Files
import csv

#File Path To Target CSV File (Election Data)
pypoll_csvpath = os.path.join("Resources", "election_data.csv")

#Store CSV File Data
voter_identification = [] #Store Ballot IDs Directly From CSV File
candidates_repeated = [] #Store Candidate Choices Directly From CSV File
counties_repeated = [] #Store Participating Counties Directly From CSV File

#Open election_data CSV File Through Variable pypoll_csvpath
with open(pypoll_csvpath) as pypoll_csvfile:

    #Create CSV Reader Object Using CSV Module
    pypoll_csvreader = csv.reader(pypoll_csvfile, delimiter=',')

    #Read CSV File Header Row First, Store As Variable Then Skip
    pypoll_csv_header = next(pypoll_csvreader)

    #Read All Rows Following Header, Storing Associated Values
    for row in pypoll_csvreader:
        voter_identification_numbers = row[0]
        voter_identification.append(voter_identification_numbers)
        counties_repeated_designation = row[1]
        counties_repeated.append(counties_repeated_designation)
        candidates_repeated_designation = row[2]
        candidates_repeated.append(candidates_repeated_designation)

    #Extract Unique Candidates/Counties In Alphabetical Order
    candidates = sorted(list(set(candidates_repeated)))
    counties = sorted(list(set(counties_repeated)))

    #Convert counties List To Single List With All Unique Counties
    counties_string = ', '.join(counties)

    #Create Dictionaries Storing Running Vote Tally For Each Candidate & Associated Percentages
    candidate_running_vote_tally = {candidate: 0 for candidate in candidates}
    candidate_vote_percentages = {}

    #Iterate Through candidate_repeated List Containing All Voter Candidate Selections
    for candidate_selection in candidates_repeated:

        #Check If Candidate Selected Belongs To Unique Candidates List
        if candidate_selection in candidates:

            #Update Running Tally For This Candidate
            candidate_running_vote_tally[candidate_selection] += 1
    
    #Determine Total Number Of Votes Cast
    total_votes = len(voter_identification)

    #Specify Location & Create New Text File Containing Same Results
    PyPoll_Results_path = os.path.join("Analysis", "PyPoll_Results.txt")
    
    #Write Text File To Input Results
    with open(PyPoll_Results_path, 'w') as output_file:

        #Print Statements For Results Display In Terminal
        print("\nElection Results")
        print(" ")
        print("----------------------------")
        print(" ")
        print("Total Votes:", "{:,}".format(total_votes))
        print(" ")
        print("Participating Counties:", counties_string)
        print(" ")
        print("----------------------------")
        print(" ")

        #Print Statements To Input Results Into Text File
        print("Election Results", file=output_file)
        print(" ", file=output_file)
        print("----------------------------", file=output_file)
        print(" ", file=output_file)
        print("Total Votes:", "{:,}".format(total_votes), file=output_file)
        print(" ", file=output_file)
        print("Participating Counties:", counties_string, file=output_file)
        print(" ", file=output_file)
        print("----------------------------", file=output_file)
        print(" ", file=output_file)

        #Use Total Number Of Votes Cast For Percentage Calculations
        for candidate, votes_received in candidate_running_vote_tally.items():
            votes_received_percentage = (votes_received/total_votes) * 100
            candidate_vote_percentages[candidate] = votes_received_percentage
            formatted_candidate_vote_percentages = f"{votes_received_percentage:.3f}"

            #Print Statement For All Candidate Results In Termianl
            print(f"{candidate}: {formatted_candidate_vote_percentages}% votes received ({votes_received:,} votes)\n")

            #Print Statement For All Candidate Results In Text File
            print(f"{candidate}: {formatted_candidate_vote_percentages}% votes received ({votes_received:,} votes)\n", file=output_file)

        #Determine Winner Of Election
        winning_candidate = max(candidate_running_vote_tally, key=candidate_running_vote_tally.get)

        #Print Statement To Display Winner Of Election In Terminal
        print("----------------------------")
        print(" ")
        print(f"Election Winner: {winning_candidate}")
        print(" ")
        print("----------------------------")

        #Print Statement To Input Winner Of Election Into Text File
        print("----------------------------", file=output_file)
        print(" ", file=output_file)
        print(f"Election Winner: {winning_candidate}", file=output_file)
        print(" ", file=output_file)
        print("----------------------------", file=output_file)
