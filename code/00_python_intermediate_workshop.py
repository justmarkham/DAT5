## QUIZ TO REVIEW BEGINNER WORKSHOP

a = 5
b = 5.0
c = a/2
d = b/2

# What is type(a)?
# What is type(b)?
# What is c?
# What is d?

e = [a, b]
f = range(10)

# What is type(e)?
# What is len(e)?
# What is type(f)?
# What are the contents of f?
# What is 'range' called?
# How do I get help on 'range'?

g = ['mon','tues','wed','thurs','fri']

# How do I slice out 'mon'?
# How do I slice out 'mon' through 'wed'?
# What are two ways to slice out 'fri'?
# How do I check the type of 'mon'?

g.remove('wed')
sorted(g)
h = sorted(g, reverse=True)

# What are the contents of g?
# What are the contents of h?
# What is 'remove' called?
# How do I get help on 'remove'?
# What is 'reverse=True' called?

i = 'Hello'
j = 'friend'
k = i + j
l = i + 3
m = i[0]

# What is 'k'?
# What is 'l'?
# What is 'm'?



## FOR LOOPS AND BASIC LIST COMPREHENSIONS

# print 1 through 5
nums = range(1, 6)
for num in nums:
    print num

# for loop to create a list of cubes
cubes = []
for num in nums:
    cubes.append(num**3)

# equivalent list comprehension
cubes = [num**3 for num in nums]    # [1, 8, 27, 64, 125]

# EXERCISE:
# Given that: letters = ['a','b','c']
# Write a list comprehension that returns: ['A','B','C']

# BONUS EXERCISE:
# Given that: word = 'abc'
# Write a list comprehension that returns: ['A','B','C']



## LIST COMPREHENSIONS WITH CONDITIONS

# for loop to create a list of cubes of even numbers
cubes_of_even = []
for num in nums:
    if num % 2 == 0:
        cubes_of_even.append(num**3)

# equivalent list comprehension
# syntax: [expression for variable in iterable if condition]
cubes_of_even = [num**3 for num in nums if num % 2 == 0]    # [8, 64]



## DICTIONARIES

# dictionaries are similar to lists:
# - both can contain multiple data types
# - both are iterable
# - both are mutable

# dictionaries are different from lists:
# - dictionaries are unordered
# - dictionaries are made of key-value pairs
# - dictionary keys must be unique

# create a dictionary (and open Variable Explorer in Spyder)
family = {'dad':'homer', 'mom':'marge', 'size':6}

# examine a dictionary
family[0]           # throws an error (there is no ordering)
family['dad']       # returns 'homer'
len(family)         # returns 3
family.keys()       # returns list: ['dad', 'mom', 'size']
family.values()     # returns list: ['homer', 'marge', 6]
family.items()      # returns list of tuples:
                    #   [('dad', 'homer'), ('mom', 'marge'), ('size', 6)]
'mom' in family     # returns True
'marge' in family   # returns False (only checks keys)

# modify a dictionary
family['cat'] = 'snowball'          # add a new entry
family['cat'] = 'snowball ii'       # edit an existing entry
del family['cat']                   # delete an entry
family['kids'] = ['bart', 'lisa']   # value can be a list

# accessing a list element within a dictionary
family['kids'][0]   # returns 'bart'

# EXERCISE:
# Given that: d = {'a':10, 'b':20, 'c':[30, 40]}
# First, print the value for 'a'
# Then, change the value for 'b' to be 25
# Then, change the 30 to be 35
# Finally, append 45 to the end of the list that contains 35 and 40

# BONUS EXERCISE:
# Write a list comprehension that returns a list of the keys in uppercase



## APIs

# API Providers: https://apigee.com/providers
# Echo Nest API Console: https://apigee.com/console/echonest
# Echo Nest Developer Center: http://developer.echonest.com/

import requests     # import module (make its functions available)

# use requests to talk to the web
r = requests.get('http://www.google.com')
r.text
type(r.text)

# request data from the Echo Nest API
r = requests.get('http://developer.echonest.com/api/v4/artist/top_hottt?api_key=KBGUPZPJZS9PHWNIN&format=json')
r.text
r.json()        # decode JSON
type(r.json())
top = r.json()

# pretty print for easier readability
import pprint
pprint.pprint(top)

# pull out the artist data
artists = top['response']['artists']    # list of 15 dictionaries

# reformat data into a table structure
artists_header = artists[0].keys()                      # list of 2 strings
artists_data = [artist.values() for artist in artists]  # list of 15 lists



## WORKING WITH PUBLIC DATA

# List of data sources: https://github.com/justmarkham/DAT5/blob/master/other/public_data.md
# FiveThirtyEight: http://fivethirtyeight.com/
# FiveThirtyEight data: https://github.com/fivethirtyeight/data
# NFL ticket prices data: https://github.com/fivethirtyeight/data/tree/master/nfl-ticket-prices

# open a downloaded CSV file
import csv
with open('2014-average-ticket-price.csv', 'rU') as f:
    data = [row for row in csv.reader(f)]

# open a CSV file from a URL
r = requests.get('https://raw.githubusercontent.com/fivethirtyeight/data/master/nfl-ticket-prices/2014-average-ticket-price.csv')
data = [row for row in csv.reader(r.iter_lines())]

# examine the data
type(data)
len(data)
data[0]
data[1]

# save the data we want
data = data[1:97]

# Question: What is the average ticket price for Ravens' home vs away games?

# step 1: create a list that only contains events
data[0][0]
data[1][0]
data[2][0]
events = [row[0] for row in data]

# EXERCISE
# step 2: create a list that only contains prices (stored as integers)
prices = [int(row[2]) for row in data]

# step 3: figure out how to locate the away teams
events[0]
events[0].find(' at ')
stop = events[0].find(' at ')
events[0][:stop]

# step 4: use a for loop to make a list of the away teams
away_teams = []
for event in events:
    stop = event.find(' at ')
    away_teams.append(event[:stop])

# EXERCISE
# step 5: use a for loop to make a list of the home teams
home_teams = []
for event in events:
    start = event.find(' at ') + 4
    stop = event.find(' Tickets ')
    home_teams.append(event[start:stop])

# step 6: create a list of the Ravens home game prices
zip(home_teams, prices)
[pair for pair in zip(home_teams, prices)]
[pair[1] for pair in zip(home_teams, prices)]
[price for team, price in zip(home_teams, prices)]
[price for team, price in zip(home_teams, prices) if team == 'Baltimore Ravens']
ravens_home = [price for team, price in zip(home_teams, prices) if team == 'Baltimore Ravens']

# step 7: create a list of the Ravens away game prices
ravens_away = [price for team, price in zip(away_teams, prices) if team == 'Baltimore Ravens']

# EXERCISE
# step 8: calculate the average of each list
float(sum(ravens_home)) / len(ravens_home)
float(sum(ravens_away)) / len(ravens_away)
