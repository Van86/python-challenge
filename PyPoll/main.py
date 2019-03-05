import os
import csv

#initialize variables
total_votes = 0
vote_counts = 0
winner_count = 0
Winner = ""
vote_percentage = 0
candidates = {}
candidate = ""

#I gave this one my dardenst 


PollData = '/Users/vanjoisscott/Desktop/python-challenge/PyPoll/election_data.csv'

#open the file
with open(PollData, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip the header
    row = next(csvreader)

    for row in csvreader:

        #add to total number of votes
        candidates = row[2]
        total_votes = total_votes + 1

        #if candidate has other votes then add to vote tally
        if candidates in vote_counts:
            vote_counts[candidate] = vote_counts[candidate] + 1
        else:
            vote_counts[candidate] + 1

percentages = []
max_votes = vote_counts[0]
max_index = 0
#find percentage of vote for each candidate
for count in range(len(candidates)):
    vote_percentage = vote_counts[count]/num_votes*100
    percentages.append(vote_percentage)
    if vote_counts[count] > max_votes:
        max_votes = vote_counts[count]
        print(max_votes)
        max_index = count
winner = candidates[max_index]

#print results
print("Election Results")
print("--------------------------")
print("Total Votes: " , total_votes)
for count in range(len(candidates)):
    vote_percentage[index] = round((vote_counts[index]/total_votes)*100,2) 
    print( candidates[index] +  ": " + str(vote_percentage[index]) + "% (" + str(vote_counts[index]) + ")")
print("---------------------------")
print("Winner: {winner}")
print("---------------------------")


#open write file
f = open("PyPoll.txt", mode = 'w')

f.write("Election Results " + "\n")
f.write("-------------------------- "+ "\n")
f.write("Total Votes: + {total_votes} "+ "\n")
for count in range(len(candidates)):
    f.write("{candidates[count]}: {vote_percentage[count]}% ({vote_counts[count]}) "+ "\n")
f.write("--------------------------- + ""\n")
f.write("Winner: {winner}\n")
f.write("--------------------------- "+ "\n")

f.close()