import csv
import pyfpgrowth as fpg


# Task 1 
data = csv.reader(open('www.csv',mode='r'),delimiter='\t')

'''
for i in range(3):
    row = next(data)
    print(row)
'''
rowID = 0
QueryList=[]
for row in data:
    if not rowID:
        KeywordsList = row[2:]
    else:
        try:
            QueryList.append(row[1].split(' '))
        except IndexError: #Skip blank row
            pass
    rowID+=1

print(f'Number of attributes: {len(KeywordsList)}')
print(f'Number of records: {len(QueryList)}')

# Task 2
patterns = fpg.find_frequent_patterns(QueryList,100)
print(patterns)

# Task 3
for minSupportCount in range(10,100,10):
    patterns = fpg.find_frequent_patterns(QueryList,minSupportCount)
    print('-'*100)
    print(f'minSupportCount is {str(minSupportCount)}, number of found frequent itemset: {str(len(patterns))}')
    print(patterns)
    print('-'*100)

# Task 4 
# set minSupportCount to 40
minSupportCount = 40
patterns = fpg.find_frequent_patterns(QueryList,minSupportCount)


















