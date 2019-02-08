import os
csvpath=os.path.join('Resources','election_data.csv')

# define lists to store data columns
vid = []
county = []
candidate = []

import csv

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # store data into seperate lists  
    for row in csvreader:
        vid.append(int(row[0]))
        county.append(str(row[1]))
        candidate.append(str(row[2]))

    # number of vote is stored below:
    total_vote=int(len(vid))
   
    # unique is a list of [None], so we just print can_list
    # can_list contains our unique list of candidates
    can_list=[]
    unique=[can_list.append(x) for x in candidate if x not in can_list]
    
    # create a dictionary to store one list for each candidate with their name
    # create a list of number of votes and percentage of votes
    votes={}
    num_votes=[]
    percent_votes=[]

    # find the vote number and percentage for each candidate and store them into two lists
    for can in can_list:
        votes[can]=[]
        
        for y in candidate:
            if y==can:
                votes[can].append(y)

        num_votes.append(len(votes[can]))  
        percent_votes.append('{0:.3f}%'.format(len(votes[can])/total_vote*100))
    
    # find the winner and return his name to winner
    max_num=0
    for j in range(len(num_votes)):
       
        if max_num<num_votes[j]:
             max_num=num_votes[j]
             winner=can_list[j]

# Store results into a list results[]

results=[]
results.append("Election Results")
results.append("--------------------------")
results.append("Total Votes: "+str(total_vote))
results.append("--------------------------")

for k in range(len(can_list)):
    results.append(can_list[k]+": "+percent_votes[k]+" ("+str(num_votes[k])+")")

results.append("--------------------------")
results.append("Winner: "+winner)
results.append("--------------------------")

# print out the results
for item in results:
    print(item)

# output the results to result_pypoll.txt
output_path=os.path.join('output','result_pypoll.txt')

with open(output_path, 'w') as txtfile:
    for item in results:
        txtfile.write("{}\n".format(item))
        

