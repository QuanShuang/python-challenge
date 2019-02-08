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
    # print (total_vote)
    # print (can_list)
    
    # create a dictionary to store one list for each candidate with their name
    votes={}
    num_votes={}
    percent_votes={}

    for can in can_list:
        votes[can]=[]
        
        for y in candidate:
            if y==can:
                votes[can].append(y)

        num_votes[can]=len(votes[can])    
        percent_votes[can]=format(len(votes[can])/total_vote,"0.000%")

        # winner=(x for can in can_list if )



results=[]
results.append("Election Results")
results.append("--------------------------")

for can in can_list:
    results.append(str(can)+": "+str(percent_votes[can])+"("+str(num_votes[can])+")")

    

results.append("--------------------------")




# results.append("")

# results.append("Total Votes: "+str(total_vote))
# results.append("Total: $"+str(ttl))
# results.append("Average Change: $"+format(avr_changes,".2f"))
# results.append("Greatest Increase in Profits: "+str(max_month)+ " ($" + str(max_changes)+")")
# results.append("Greatest Decrease in Profits: "+ str(min_month)+ " ($" + str(min_changes)+")")


for item in results:
    print(item)


# output_path=os.path.join('output','result_pybank.txt')

# with open(output_path, 'w') as txtfile:
#     for item in results:
#         txtfile.write("{}\n".format(item))
        

