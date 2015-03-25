'''
SOLUTION FILE: Homework with Chipotle data
https://github.com/TheUpshot/chipotle
'''


'''
PART 1: read in the data, parse it, and store it in a list of lists called 'data'
Hint: this is a tsv file, and csv.reader() needs to be told how to handle it
'''

import csv

# specify that the delimiter is a tab character
with open('chipotle_orders.tsv', 'rU') as f:
    data = [row for row in csv.reader(f, delimiter='\t')]


'''
PART 2: separate the header and data into two different lists
'''

header = data[0]
data = data[1:]


'''
PART 3: calculate the average price of an order
Hint: examine the data to see if the 'quantity' column is relevant to this calculation
Hint: work smarter, not harder! (this can be done in a few lines of code)
'''

# count the number of unique order_id's
# note: you could assume this is 1834 because that's the maximum order_id, but it's best to check
num_orders = len(set([row[0] for row in data]))     # 1834

# create a list of prices
# note: ignore the 'quantity' column because the 'item_price' takes quantity into account
prices = [float(row[4][1:-1]) for row in data]      # strip the dollar sign and trailing space

# calculate the average price of an order and round to 2 digits
round(sum(prices) / num_orders, 2)      # $18.81


'''
PART 4: create a list (or set) of all unique sodas and soft drinks that they sell
Note: just look for 'Canned Soda' and 'Canned Soft Drink', and ignore other drinks like 'Izze'
'''

# if 'item_name' includes 'Canned', append 'choice_description' to 'sodas' list
sodas = []
for row in data:
    if 'Canned' in row[2]:
        sodas.append(row[3][1:-1])      # strip the brackets

# create a set of unique sodas
unique_sodas = set(sodas)


'''
PART 5: calculate the average number of toppings per burrito
Note: let's ignore the 'quantity' column to simplify this task
Hint: think carefully about the easiest way to count the number of toppings
Hint: 'hello there'.count('e')
'''

# keep a running total of burritos and toppings
burrito_count = 0
topping_count = 0

# calculate number of toppings by counting the commas and adding 1
# note: x += 1 is equivalent to x = x + 1
for row in data:
    if 'Burrito' in row[2]:
        burrito_count += 1
        topping_count += (row[3].count(',') + 1)

# calculate the average topping count and round to 2 digits
round(topping_count / float(burrito_count), 2)      # 5.40


'''
PART 6: create a dictionary in which the keys represent chip orders and
  the values represent the total number of orders
Expected output: {'Chips and Roasted Chili-Corn Salsa': 18, ... }
Note: please take the 'quantity' column into account!
Advanced: learn how to use 'defaultdict' to simplify your code
'''

# start with an empty dictionary
chips = {}

# if chip order is not in dictionary, then add a new key/value pair
# if chip order is already in dictionary, then update the value for that key
for row in data:
    if 'Chips' in row[2]:
        if row[2] not in chips:
            chips[row[2]] = int(row[1])     # this is a new key, so create key/value pair
        else:
            chips[row[2]] += int(row[1])    # this is an existing key, so add to the value

# defaultdict saves you the trouble of checking whether a key already exists
from collections import defaultdict
dchips = defaultdict(int)
for row in data:
    if 'Chips' in row[2]:
        dchips[row[2]] += int(row[1])


'''
BONUS: think of a question about this data that interests you, and then answer it!
'''
