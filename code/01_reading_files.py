'''
Lesson on file reading using Airline Safety Data
https://github.com/fivethirtyeight/data/tree/master/airline-safety
'''

# read the whole file at once, return a single string (including newlines)
# 'rU' mode (read universal) converts different line endings into '\n'
f = open('airline_safety.csv', 'rU')
data = f.read()
f.close()

# use a context manager to automatically close your file
with open('airline_safety.csv', 'rU') as f:
    data = f.read()

# read the whole file at once, return a list of lines
with open('airline_safety.csv', 'rU') as f:
    data = f.readlines()

# use list comprehension to duplicate readlines
with open('airline_safety.csv', 'rU') as f:
    data = [row for row in f]

# use the csv module to create a list of lists
import csv
with open('airline_safety.csv', 'rU') as f:
    data = [row for row in csv.reader(f)]

# alternative method that doesn't require downloading the file
import requests
r = requests.get('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
data = [row for row in csv.reader(r.iter_lines())]

# separate the header and data
header = data[0]
data = data[1:]

# EXERCISE:
# create a list of airline names (without the star)
# create a list of the same length that contains 1 if there's a star and 0 if not
airlines = []
starred = []
for row in data:
    if row[0][-1] == '*':
        starred.append(1)
        airlines.append(row[0][:-1])
    else:
        starred.append(0)
        airlines.append(row[0])

# EXERCISE:
# create a list that contains the average number of incidents per distance
[(int(row[2]) + int(row[5])) / float(row[1])  for row in data]


'''
A few extra things that will help you with the homework
'''

# 'in' statement is useful for lists
my_list = [1, 2, 1]
1 in my_list            # True
3 in my_list            # False

# 'in' is useful for strings (checks for substrings)
my_string = 'hello there'
'the' in my_string      # True
'then' in my_string     # False

# 'in' is useful for dictionaries (checks keys but not values)
my_dict = {'name':'Kevin', 'title':'instructor'}
'name' in my_dict       # True
'Kevin' in my_dict      # False

# 'set' data structure is useful for gathering unique elements
set(my_list)            # returns a set of 1, 2
len(set(my_list))       # count of unique elements


'''
Homework with Chipotle data
https://github.com/TheUpshot/chipotle
'''

'''
PART 1: read in the data, parse it, and store it in a list of lists called 'data'
Hint: this is a tsv file, and csv.reader() needs to be told how to handle it
'''

'''
PART 2: separate the header and data into two different lists
'''

'''
PART 3: calculate the average price of an order
Hint: examine the data to see if the 'quantity' column is relevant to this calculation
Hint: work smarter, not harder! (this can be done in a few lines of code)
'''

'''
PART 4: create a list (or set) of all unique sodas and soft drinks that they sell
Note: just look for 'Canned Soda' and 'Canned Soft Drink', and ignore other drinks like 'Izze'
'''

'''
PART 5: calculate the average number of toppings per burrito
Note: let's ignore the 'quantity' column to simplify this task
Hint: think carefully about the easiest way to count the number of toppings
Hint: 'hello there'.count('e')
'''

'''
PART 6: create a dictionary in which the keys represent chip orders and
  the values represent the total number of orders
Expected output: {'Chips and Roasted Chili-Corn Salsa': 18, ... }
Note: please take the 'quantity' column into account!
Advanced: learn how to use 'defaultdict' to simplify your code
'''

'''
BONUS: think of a question about this data that interests you, and then answer it!
'''
