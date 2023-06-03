# import modules
import os
import csv

# path to collect data from the recource folder
election_datacsv = os.path.join("Resources", "election_data.csv") 
election_output = os.path.join("Analysis", "election_result.txt") 
# open file
total_votes = 0
candidate_list = []
candidate_votes = {}
vote_value = 0
winning_vote = 0
#Total votes
with open (election_datacsv) as csvfile:
    csv_reader = csv.reader(csvfile)
    header = next(csv_reader)
    for row in csv_reader:
        #print(row)
        total_votes += 1 
        candidate_name = row[2]        
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
vote_results = f""" 
Election Results
----------------
Total Votes: {total_votes}
----------------
""" 
print(vote_results)
with open(election_output,"w") as txt:
    txt.write(vote_results)  
    for key in candidate_votes:
        vote_value = candidate_votes.get(key)
        vote_percent = vote_value/total_votes * 100
        if vote_value > winning_vote:
            winning_vote = vote_value
            winning_candidate = key
        results = f"""{key}: {vote_percent:.3f}% ({vote_value})\n""" 
        print(results)
        txt.write(results)
    Winner = f"""--------------------
Winner: {winning_candidate}
------------------------
"""
    print(Winner)
    txt.write(Winner)


