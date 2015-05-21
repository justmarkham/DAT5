'''
Regular Expressions Exercise
'''

# open file and store each line as one row
with open('../data/homicides.txt', 'rU') as f:
    raw = [row for row in f]


'''
Create a list of ages 
'''

import re

ages = []
for row in raw:
    match = re.search(r'\d+ years old', row)
    if match:
        ages.append(match.group())
    else:
        ages.append('0')

# split the string on spaces, only keep the first element, and convert to int
ages = [int(element.split()[0]) for element in ages]

# check that 'raw' and 'ages' are the same length
assert(len(raw)==len(ages))

# simplify process using a lookahead
ages = []
for row in raw:
    match = re.search(r'\d+(?= years)', row)
    if match:
        ages.append(int(match.group()))
    else:
        ages.append(0)
