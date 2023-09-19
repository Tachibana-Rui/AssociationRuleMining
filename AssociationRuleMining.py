import csv
import pyfpgrowth_modified as fpg

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
            QueryList.append(set(row[1].split(' ')))
        except IndexError: #Skip blank row
            pass
    rowID+=1

wordset = set(i for q in QueryList for i in q)
#print(f'Number of attributes from header of database: {len(KeywordsList)}')
print(f'Number of attributes from user queries: {len(wordset)}')
print(f'Number of records: {len(QueryList)}')

# Task 2
patterns = fpg.find_frequent_patterns(QueryList,100)
print('-'*100)
print(f'minSupportCount is 100, number of found frequent itemset: {str(len(patterns))}')
print(patterns)
print('-'*100)

# Task 3
def max_frequent_itemset_size(patterns:dict):
    maxSize = 0
    for itemset in patterns.keys():
        if len(itemset)>maxSize:
            maxSize = len(itemset) 
    return maxSize

for minSupportCount in range(10,101,10):
    patterns = fpg.find_frequent_patterns(QueryList,minSupportCount)
    maxSize = max_frequent_itemset_size(patterns)
#    print('-'*100)
    print(f'min-support is {str(minSupportCount/10000)}, number of found frequent itemset: {str(len(patterns))}, maximum size of frequent itemsets: {str(maxSize)}')
#    print(patterns)
#    print('-'*100)


# Task 4 
minSupportCount = 40
confidence_threshold = 0.2
patterns = fpg.find_frequent_patterns(QueryList,minSupportCount)
rules = fpg.generate_association_rules(patterns,confidence_threshold)
print(f'Rule count: {str(len(rules))}')
#print(rules)

# Task 5
for i in range(5):
    confidence_threshold = 0.1+(1-0.1)/4*i
    patterns = fpg.find_frequent_patterns(QueryList,minSupportCount)
    rules = fpg.generate_association_rules(patterns,confidence_threshold)
    print(f'min-confidence = {confidence_threshold}, number of rules: {len(rules)}')

# Task 6
minSupportCount = 10
confidence_threshold = 0.2
patterns = fpg.find_frequent_patterns(QueryList,minSupportCount)
#print(patterns)
rules = fpg.generate_association_rules(patterns,confidence_threshold,len(QueryList))
'''
print('-'*100)
for k in rules.keys():
    print(f'{k} -> {rules[k][0]} : conf={rules[k][1]}, lift={rules[k][2]}')
print('-'*100)
'''
def isInRange(n,nRange:tuple):
    return True if n >= nRange[0] and n <= nRange[1] else False
    
def filterRules(rules:dict, confidenceRange:tuple, liftRange:tuple, sort_by = None, reverseFlag = True):
    filteredRules=[]
    for rule in rules.items():
        if isInRange(rule[1][1], confidenceRange) and isInRange(rule[1][2], liftRange):
            filteredRules.append(rule)
    if sort_by == 'confidence':
        filteredRules.sort(key = lambda rule:rule[1][1], reverse = reverseFlag)
    elif sort_by == 'lift':
        filteredRules.sort(key = lambda rule:rule[1][2], reverse = reverseFlag) 
    return filteredRules

def showRules(filteredRules: list, showConfidence = True, showLift = True, showSupportX = False, showSupportY = False):
    for rule in filteredRules:
        if showConfidence: confStr = f'confidence={rule[1][1]} '
        else: confStr = ''

        if showLift: liftStr = f'lift={rule[1][2]} '
        else: liftStr = ''

        if showSupportX: showSupportXStr = f'support_X={rule[1][3]} ' 
        else: showSupportXStr = ''

        if showSupportY:showSupportYStr = f'support_Y={rule[1][4]} '
        else: showSupportYStr = ''            

        print(f'{rule[0]} -> {rule[1][0]}: '+confStr+liftStr+showSupportXStr+showSupportYStr)

print('-'*100)
print(showRules(filterRules(rules,confidenceRange = [0.8,1.0],liftRange = [100,1000],sort_by = 'confidence')))
print('-'*100)

print('-'*100)
print(showRules(filterRules(rules,confidenceRange = [0.2,0.5],liftRange = [2,10],sort_by = 'confidence')))
print('-'*100)

















