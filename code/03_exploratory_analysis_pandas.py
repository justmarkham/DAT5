# -*- coding: utf-8 -*-
"""
CLASS: Pandas for Data Exploration, Analysis, and Visualization

About the data:
WHO alcohol consumption data:
    article: http://fivethirtyeight.com/datalab/dear-mona-followup-where-do-people-drink-the-most-beer-wine-and-spirits/    
    original data: https://github.com/fivethirtyeight/data/tree/master/alcohol-consumption
    files: drinks.csv (with additional 'continent' column)

"""

"""
First, we need to import Pandas into Python.  Pandas is a Python package that
allows for easy manipulation of data frames.  You'll also need to import 
matplotlib for plotting.
"""

#imports
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


'''
Reading Files, Summarizing, Selecting, Filtering, Sorting, Detecting Duplicates
'''
# Can read a file from from a local file on your computer or from a URL
drinks = pd.read_table('drinks.csv', sep=',')   # read_table is more general
drinks = pd.read_csv('drinks.csv')  # read_csv is specific to CSV and implies sep=","
# Can also read from URLs
drinks = pd.read_csv(REPLACE)


'''
Key Concept: Dot notation
In Python, you can think of an object as an entity that can have both attributes
and methods.  A dot following an object indicates that you are about to access
somehing within the object, an attribute or a method.  Attributes contain
information abut the object.  They are usually a single "word" following the
dot.  A method is somethng the object can do.  They are usually a "word" with
paentheses following the dot.
'''

# examine the drinks data
drinks                          # print the first 30 and last 30 rows
type(drinks)                    # DataFrame
drinks.head()                   # print the first 5 rows
drinks.head(10)                 # printthe first 10 rows
drinks.tail()                   # print the last 5 rows
drinks.describe()               # summarize all numeric columns
drinks.describe(include='all')  # includes non numeric columns; new in pandas 0.15.0
drinks.index                    # "the index" (aka "the labels")
drinks.columns                  # column names (which is "an index")
drinks.dtypes                   # data types of each column
drinks.shape                    # number of rows and columns
drinks.values                   # underlying numpy array
drinks.info()                   # concise summary (includes memory usage as of pandas 0.15.0)

# Print the 'beer_servings' Series (a single column)
drinks.beer_servings
drinks['beer_servings']
type(drinks.beer_servings)    

# Print two columns
drinks[['beer_servings','wine_servings']] 
cols = ['beer_servings','wine_servings']
drinks[cols]

# Calculate the average 'beer_servings' for the entire dataset
drinks.describe()                   # summarize all numeric columns
drinks.beer_servings.describe()     # summarize only the 'beer_servings' Series
drinks.beer_servings.mean()         # only calculate the mean
drinks.beer_servings.max()          # only calcuate the max
drinks.beer_servings.min()          # only calculate the min

# Other aggregation functions
drinks.beer_servings.sum()           
drinks.beer_servings.count()
float(drinks.beer_servings.sum())/drinks.beer_servings.count()

# Count the number of occurrences of each 'continent' value
drinks.continent.value_counts()

# Simple logical filters
# Print all columns, but only show rows where the country is in Europe
# Let's look at each piece of this.
drinks.continent                    # Returns out all of the continent values
drinks.continent=='EU'              # Returns True/False list
drinks[drinks.continent=='EU']      # Returns all rows where True

# Other logical filters
drinks[drinks.beer_servings > 158]
drinks[drinks.beer_servings <= 10]
type(drinks[drinks.beer_servings <= 10])    # Dataframe
drinks[drinks.beer_servings <= 10][['country','beer_servings']]

# Calculate the average 'beer_servings' for all of Europe
drinks[drinks.continent=='EU'].beer_servings.mean()

# More complex logical fitering
# Only show European countries with 'wine_servings' greater than 300
drinks[(drinks.continent=='EU') & (drinks.wine_servings > 300)]

# Show European countries or countries 'wine_servings' greater than 300
drinks[(drinks.continent=='EU') | (drinks.wine_servings > 300)]

# Show countries who have more than the mean beer_servings
drinks[drinks.beer_servings > drinks.beer_servings.mean()]

##########################################
############    Exercise 1    ############
##########################################

# Using the 'drinks' data, answer te following questions:
# 1. What is the maximum number of total litres of pure alcohol?


# 2. Which country has the maximum number of total litres of pure alcohol?


# 3. Does Haiti or Belarus consume more servings of spirits?


# 4. How many countries have more than 300 wine servings OR more than 300 
# beer servings OR more than 300 spirit serving?


# 5. For the countries in the previous question, what is the average total litres
# of pure alcohol? 



# sorting
drinks.beer_servings.order()                              # only works for a Series
drinks.sort_index()                                       # sort rows by label
drinks.sort_index(by='beer_servings')                     # sort rows by a specific column
drinks.sort_index(by='beer_servings', ascending=False)    # use descending order instead
drinks.sort_index(by=['beer_servings', 'wine_servings'])  # sort by multiple columns

# Determine which 10 countries have the highest 'total_litres_of_pure_alcohol'
drinks.sort_index(by='total_litres_of_pure_alcohol').tail(10)

# Determine which country has the highest value for 'beer_servings'
drinks[drinks.beer_servings==drinks.beer_servings.max()].country

# Use dot notation to string together commands
# How many countries in each continent have beer_servings greater than 182?
# i.e. a beer every two days
drinks[drinks.beer_servings > 182].continent.value_counts().sort_index()

# add a new column as a function of existing columns
# note: can't (usually) assign to an attribute (e.g., 'drinks.total_servings')
drinks['total_servings'] = drinks.beer_servings + drinks.spirit_servings + drinks.wine_servings
drinks['alcohol_mL'] = drinks.total_litres_of_pure_alcohol * 1000
drinks.head()

'''
Split-Apply-Combine
'''

# for each continent, calculate mean beer servings
drinks.groupby('continent').beer_servings.mean()

# for each continent, calculate mean of all numeric columns
drinks.groupby('continent').mean()

# for each continent, count number of occurrences
drinks.groupby('continent').continent.count()
drinks.continent.value_counts()


'''
A little numpy
'''
probs = np.array([0.51, 0.50, 0.02, 0.49, 0.78])
# np.where functions like an IF statement in Excel
# np.where(condition, value if true, value if false)
np.where(probs >= 0.5, 1, 0)
drinks['lots_of_beer'] = np.where(drinks.beer_servings > 300, 1, 0)



##########################################
############    Exercise 2    ############
##########################################

# 1. What is the average number of total liters of pure alcohol for each 
# continent?



# 2. For each continent, calculate the mean wine_servings for all countries who 
# have a a spirit_servings greater than the overall spirit_servings mean.



# 3. Per continent, for all of the countries that drink more beer servings than 
# the average number of beer servings, what is the average number of wine 
# servings?



'''
Plotting
'''

# bar plot of number of countries in each continent
drinks.continent.value_counts().plot(kind='bar', title='Countries per Continent')
plt.xlabel('Continent')
plt.ylabel('Count')
plt.show()                                  # show plot window (if it doesn't automatically appear)
plt.savefig('countries_per_continent.png')  # save plot to file

# bar plot of average number of beer servings (per adult per year) by continent
drinks.groupby('continent').beer_servings.mean().plot(kind='bar', title='Average Number of Beer Servings By Continent')
plt.ylabel('Average Number of Beer Servings Per Year')
plt.show()

# histogram of beer servings (shows the distribution of a numeric column)
drinks.beer_servings.hist(bins=20)
plt.title("Distribution of Beer Servings")
plt.xlabel('Beer Servings')
plt.ylabel('Frequency')
plt.show()

# density plot of beer servings (smooth version of a histogram)
drinks.beer_servings.plot(kind='density', xlim=(0,500))
plt.title("Distribution of Beer Servings")
plt.xlabel('Beer Servings')
plt.show()

# grouped histogram of beer servings (shows the distribution for each group)
drinks.beer_servings.hist(by=drinks.continent)
plt.show()

drinks.beer_servings.hist(by=drinks.continent, sharex=True)
plt.show()

drinks.beer_servings.hist(by=drinks.continent, sharex=True, sharey=True)
plt.show()

drinks.beer_servings.hist(by=drinks.continent, sharey=True, layout=(2, 3))   # change layout (new in pandas 0.15.0)
plt.show()

# boxplot of beer servings by continent (shows five-number summary and outliers)
drinks.boxplot(column='beer_servings', by='continent')
plt.show()

# scatterplot of beer servings versus wine servings
drinks.plot(kind='scatter', x='beer_servings', y='wine_servings', alpha=0.3)
plt.show()

# same scatterplot, except point color varies by 'spirit_servings'
# note: must use 'c=drinks.spirit_servings' prior to pandas 0.15.0
drinks.plot(kind='scatter', x='beer_servings', y='wine_servings', c='spirit_servings', colormap='Blues')
plt.show()

# same scatterplot, except all European countries are colored red
colors = np.where(drinks.continent=='EU', 'r', 'b')
drinks.plot(x='beer_servings', y='wine_servings', kind='scatter', c=colors)
plt.show()

# Scatter matrix
pd.scatter_matrix(drinks)
plt.show()


##########################################
############    Exercise 3    ############
##########################################

# 1. Generate a plot showing the average number of total litres of pure alcohol
# by continent.


# 2. Illustrate the relationship between spirit servings and total litres of 
# pure alcohol.  What kind of relationship is there?


# 3. Generate one plot that shows the distribution of spirit servings for each 
# continent.



'''
Advanced Filtering (of rows) and Selecting (of columns)
'''

# loc: filter rows by LABEL, and select columns by LABEL
drinks.loc[0]                        # row with label 0
drinks.loc[0:3]                      # rows with labels 0 through 3
drinks.loc[0:3, 'beer_servings':'wine_servings']  # rows 0-3, columns 'age' through 'occupation'
drinks.loc[:, 'beer_servings':'wine_servings']    # all rows, columns 'age' through 'occupation'
drinks.loc[[0,3], ['beer_servings','spirit_servings']]  # rows 1 and 3, columns 'age' and 'gender'

# iloc: filter rows by POSITION, and select columns by POSITION
drinks.iloc[0]                       # row with 0th position (first row)
drinks.iloc[0:3]                     # rows with positions 0 through 2 (not 3)
drinks.iloc[0:3, 0:3]                # rows and columns with positions 0 through 2
drinks.iloc[:, 0:3]                  # all rows, columns with positions 0 through 2
drinks.iloc[[0,2], [0,1]]            # 1st and 3rd row, 1st and 2nd column

# mixing: select columns by LABEL, then filter rows by POSITION
drinks.wine_servings[0:3]
drinks[['beer_servings', 'spirit_servings', 'wine_servings']][0:3]


##########################################
#############    Homework    #############
##########################################

# Prompt:  You've been asked to explore some data about about gas mileage for 
# cars and get an idea of which variables affect gas mileage.

# 1. Load the data () into a data frame.  Try looking at the "head" of the file
# in the command line to see how the file is delimited and how to load it.

# 2. Get familiar with the data.  This could include exploring some of the 
# following:
# - What is the shape of the data?  
# - What variables are available?
# - For non numeric columns, what values are in the column?
# - What are the ranges for the values in each column?
# - What is the average value for each column?  Does that different significantly
#   from the median?

# 3. Which 5 cars get the best gas mileage?  Which 5 cars with more than 4 
# cylinders get the best gas mileage?

# 4. Which 5 cars get the worst gas mileage?  Which 5 cars with 4 or fewer 
# cylinders get the worst gas mileage?

# 5. Use plots, groupby, aggregations, etc to explore the relationships 
# between mpg and the other variables.  Some examples of things you might want 
# to look at are:
# - What is the mean mpg for cars with each number of cylindres (i.e. 3 cylinders,
#   4 cylinders, 5 cylinders, etc)?
# - Did mpg rise or fall over the years contained in this dataset?
