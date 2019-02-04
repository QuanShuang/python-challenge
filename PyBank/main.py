import os

csvpath=os.path.join(..,..,..,'Instructions','PyBank','Resources','budget_data.csv')

import csv

with open(cvspath, newlines='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')


    for row in csvreader


month=[]
PandL=[]


num_month = len(month)
highest = max(PandL)
lowest = min(PandL)
ttl = sum(PandL)
avrg= 


output = (
    f"..."
    f"..."
    f".."

)

print(output)


output_path=os.path.join('output','result_pybank.txt')

with open(output_path, 'w', newlines='') as csvfile:
    csvwriter=csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['first name','last name','ssn'])
    csvwriter.writerow(['caleb','frost','505'])