import os

csvpath=os.path.join('Resources','budget_data.csv')

month = []
PnL = []
changes = []

import csv

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    for row in csvreader:
        month.append(row[0])
        PnL.append(float(row[1]))

    for i in range(len(PnL)-1):
        changes.append(float(PnL[i+1])-float(PnL[i]))
    

    num_month = len(month)
    ttl = int(sum(PnL))
    avr_changes = sum(changes)/len(changes)

    max_changes=int(max(changes))
    min_changes=int(min(changes))

    for x in range(len(changes)):
        if changes[x]==max_changes:
                # print(month[x+1])
                max_month=month[x+1]
        if changes[x]==min_changes:
                min_month=month[x+1]
                # print(month[x+1])
        

results=[]
results.append("Financial Analysis")
results.append("--------------------------")
results.append("Total Month: "+str(num_month))
results.append("Total: $"+str(ttl))
results.append("Average Change: $"+format(avr_changes,".2f"))
results.append("Greatest Increase in Profits: "+str(max_month)+ " ($" + str(max_changes)+")")
results.append("Greatest Decrease in Profits: "+ str(min_month)+ " ($" + str(min_changes)+")")


for item in results:
    print(item)


output_path=os.path.join('output','result_pybank.txt')

with open(output_path, 'w') as txtfile:
    for item in results:
        txtfile.write("{}\n".format(item))
        

