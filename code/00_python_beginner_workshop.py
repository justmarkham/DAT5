'''
Multi-line comments go between 3 quotation marks.
You can use single or double quotes.
'''

# One-line comments are preceded by the pound symbol


# BASIC DATA TYPES

x = 5               # creates an object
print type(x)       # check the type: int (not declared explicitly)
type(x)             # automatically prints
type(5)             # assigning it to a variable is not required

type(5.0)           # float
type('five')        # str
type(True)          # bool


# LISTS

nums = [5, 5.0, 'five']     # multiple data types
nums                        # print the list
type(nums)                  # check the type: list
len(nums)                   # check the length: 3
nums[0]                     # print first element
nums[0] = 6                 # replace a list element

nums.append(7)              # list 'method' that modifies the list
help(nums.append)           # help on this method
help(nums)                  # help on a list object
nums.remove('five')         # another list method

sorted(nums)                # 'function' that does not modify the list
nums                        # it was not affected
nums = sorted(nums)         # overwrite the original list
sorted(nums, reverse=True)  # optional argument

# list slicing [start:end:stride]
weekdays = ['mon','tues','wed','thurs','fri']
weekdays[0]         # element 0
weekdays[0:3]       # elements 0, 1, 2
weekdays[:3]        # elements 0, 1, 2
weekdays[3:]        # elements 3, 4
weekdays[-1]        # last element (element 4)
weekdays[::2]       # every 2nd element (0, 2, 4)
weekdays[::-1]      # backwards (4, 3, 2, 1, 0)

days = weekdays + ['sat','sun']     # concatenate lists


# FUNCTIONS

def give_me_five():         # function definition ends with colon
    return 5                # indentation required for function body

give_me_five()              # prints the return value (5)
num = give_me_five()        # assigns return value to a variable, doesn't print it

def calc(x, y, op):         # three parameters (without any defaults)
    if op == 'add':         # conditional statement
        return x + y
    elif op == 'subtract':
        return x - y
    else:
        print 'Valid operations: add, subtract'

calc(5, 3, 'add')
calc(5, 3, 'subtract')
calc(5, 3, 'multiply')
calc(5, 3)


# EXERCISE: Write a function that takes two parameters (hours and rate), and
# returns the total pay.

def compute_pay(hours, rate):
    return hours * rate

compute_pay(40, 10.50)


# EXERCISE: Update your function to give the employee 1.5 times the hourly rate
# for hours worked above 40 hours.

def compute_more_pay(hours, rate):
    if hours <= 40:
        return hours * rate
    else:
        return 40*rate + (hours-40)*(rate*1.5)

compute_more_pay(30, 10)
compute_more_pay(45, 10)


# STRINGS

# create a string
s = str(42)         # convert another data type into a string
s = 'I like you'

# examine a string
s[0]                # returns 'I'
len(s)              # returns 10

# string slicing like lists
s[:6]               # returns 'I like'
s[7:]               # returns 'you'
s[-1]               # returns 'u'

# split a string into a list of substrings separated by a delimiter
s.split(' ')        # returns ['I','like','you']
s.split()           # same thing

# concatenate strings
s3 = 'The meaning of life is'
s4 = '42'
s3 + ' ' + s4       # returns 'The meaning of life is 42'
s3 + ' ' + str(42)  # same thing


# EXERCISE: Given a string s, return a string made of the first 2 and last 2
# characters of the original string, so 'spring' yields 'spng'. However, if the
# string length is less than 2, instead return the empty string.

def both_ends(s):
    if len(s) < 2:
        return ''
    else:
        return s[:2] + s[-2:]

both_ends('spring')
both_ends('cat')
both_ends('a')


# FOR LOOPS

# range returns a list of integers
range(0, 3)     # returns [0, 1, 2]: includes first value but excludes second value
range(3)        # same thing: starting at zero is the default

# simple for loop
for i in range(5):
    print i

# print each list element in uppercase
fruits = ['apple', 'banana', 'cherry']
for i in range(len(fruits)):
    print fruits[i].upper()

# better for loop
for fruit in fruits:
    print fruit.upper()


# EXERCISE: Write a program that prints the numbers from 1 to 100. But for
# multiples of 3 print 'fizz' instead of the number, and for the multiples of
# 5 print 'buzz'. For numbers which are multiples of both 3 and 5 print 'fizzbuzz'.

def fizz_buzz():
    nums = range(1, 101)    
    for num in nums:
        if num % 15 == 0:
            print 'fizzbuzz'
        elif num % 3 == 0:
            print 'fizz'
        elif num % 5 == 0:
            print 'buzz'
        else:
            print num

fizz_buzz()


# EXERCISE: Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] returns
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.

def front_x(words):
    lista=[]
    listb=[]    
    for word in words:
        if word[0]=='x':
            lista.append(word)
        else:
            listb.append(word)
    return sorted(lista) + sorted(listb)

front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
