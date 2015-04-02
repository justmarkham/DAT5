'''
Exploratory Data Analysis Homework Solution
'''

'''
Use the automotive mpg data (https://raw.githubusercontent.com/justmarkham/DAT5/master/data/auto_mpg.csv) 
to complete the following parts.  Please turn in your code for each part.  
Before each code chunk, give a brief description (one line) of what the code is
doing (e.g. "Loads the data" or "Creates scatter plot of mpg and weight").  If 
the code output produces a plot or answers a question, give a brief
interpretation of the output (e.g. "This plot shows X,Y,Z" or "The mean for 
group A is higher than the mean for group B which means X,Y,Z").
'''

'''
Part 1
Load the data (https://raw.githubusercontent.com/justmarkham/DAT5/master/data/auto_mpg.txt) 
into a DataFrame.  Try looking at the "head" of the file in the command line
to see how the file is delimited and how to load it.
Note:  You do not need to turn in any command line code you may use.
'''

# Imports
import pandas as pd

# Reads text file and uses '|' as separator
auto = pd.read_table('https://raw.githubusercontent.com/justmarkham/DAT5/master/data/auto_mpg.txt', sep='|')
auto = pd.read_table('auto_mpg.txt', sep='|') # This is if you are reading from you computer
# Note:  This assumes that '.../DAT5/data' is your working directory.


'''
Part 2
Get familiar with the data.  Answer the following questions:
- What is the shape of the data?  How many rows and columns are there?
- What variables are available?
- What are the ranges for the values in each numeric column?
- What is the average value for each column?  Does that differ significantly
  from the median?
'''

auto.shape # There are 392 rows and 9 columns

auto.columns # This lists the column names that are available
auto.info() # This lists the column names as well as their data type.

# You can infer the range from the information available in describe
auto.describe() # This will give you the five number summary for all numeric variables
auto.min(numeric_only=True) # This will give you all of the minimums for numeric variables
auto.max(numeric_only=True) # This will give you all of the maximums for numeric variables
# You can calculate the range with the above info as shown below.
auto.max(numeric_only=True) - auto.min(numeric_only=True) # Range

auto.mean() # Means for all numeric variables
auto.median() # Medians for all numeric variables
# How much greater is the mean than the median?
auto.mean() - auto.median()
# The means are somewhat greater than the medians.


'''
Part 3
Use the data to answer the following questions:
- Which 5 cars get the best gas mileage?  
- Which 5 cars with more than 4 cylinders get the best gas mileage?
- Which 5 cars get the worst gas mileage?  
- Which 5 cars with 4 or fewer cylinders get the worst gas mileage?
'''

# 5 cars that get best gas mileage
auto.sort_index(by='mpg', ascending=False)[0:5][['car_name','mpg']]

# 5 cars with more than 4 cylinders that get the best gas mileage
auto[auto.cylinders > 4].sort_index(by='mpg', ascending=False)[0:5][['car_name','mpg']]

# 5 cars that get worst gas mileage
auto.sort_index(by='mpg')[0:5][['car_name','mpg']]

# 5 cars with 4 or fewer cylinders that get the worst gas mileage
auto[auto.cylinders > 4].sort_index(by='mpg')[0:5][['car_name','mpg']]


'''
Part 4
Use groupby and aggregations to explore the relationships 
between mpg and the other variables.  Which variables seem to have the greatest
effect on mpg?
Some examples of things you might want to look at are:
- What is the mean mpg for cars for each number of cylindres (i.e. 3 cylinders,
  4 cylinders, 5 cylinders, etc)?
- Did mpg rise or fall over the years contained in this dataset?
- What is the mpg for the group of lighter cars vs the group of heaver cars?
Note: Be creative in the ways in which you divide up the data.  You are trying
to create segments of the data using logical filters and comparing the mpg
for each segment of the data.
'''

# Mean mpg for cars for each number of cylinders
auto.groupby(by='cylinders').mpg.mean()

# Mpg usually rose over the years contianed in this dataset
auto.groupby(by='model_year').mpg.mean()

# The mpg for the gorup of lighter cars vs the group of heavier cars
# We can divide the dataset in half by the median (the lower half being the 
# lighter cars and the upper half being the heavier cars).
auto[auto.weight <= auto.weight.median()].mpg.mean() # light cars mean mpg
auto[auto.weight > auto.weight.median()].mpg.mean() # heavier cars mean mpg
# It appears that the lighter cars get better gas mileage than the heavier cars

# This question was pretty open ended, but here are some other things you could have looked at

# The average mpg for the four quartiles of displacement
# We didn't talk about the 'quantile' function in class, but it's a useful one!
auto[auto.displacement <= auto.displacement.quantile(0.25)].mpg.mean()
auto[(auto.displacement > auto.displacement.quantile(0.25)) & (auto.displacement <= auto.displacement.quantile(0.50))].mpg.mean()
auto[(auto.displacement > auto.displacement.quantile(0.50)) & (auto.displacement <= auto.displacement.quantile(0.75))].mpg.mean()
auto[auto.displacement > auto.displacement.quantile(0.75)].mpg.mean()
# It appears that as engine displacement (size) increases, the average mpg decreases.  This makes sense.

# Instead of using the somewhat complicated logic of the 'quantile', you can easily divide your dataset
# into buckets using the `cut` function.
auto.groupby(pd.cut(auto.horsepower,5)).mpg.mean()
# It appears that as horsepower increases, the average mpg decreases.  This makes sense.

auto.groupby(pd.cut(auto.acceleration, 5)).mpg.mean()
# It appears that as acceleration increases, the average mpg increases.


'''
I'll also include something I found particularly cool from Lloyd's homework.  
He wanted to look at how MPG has changed over time, but he also wanted to consider
how specific groups have changed.  He wanted to look at low, mid, and high power
cars based upon their horsepower and see how these groups have changed over time.
His code is below.  In his data, he called the original dataset 'auto'.
'''
# Now to look at how efficency has changed over time based on power and weight classes,
# two things that we know play a large role in gas mileage.  First, we create a table of
# efficeincy by power class and year.

horsey = pd.DataFrame()

# Defines low power as below 100 horsepower
horsey['low_power'] = auto[(auto.horsepower < 100)].groupby('model_year').mpg.mean()

# Defines mid power as between 100 and 150 (inclusive) horsepower
horsey['mid_power'] = auto[(auto.horsepower >= 100) & (auto.horsepower <= 150)].groupby('model_year').mpg.mean()

# Defines high power as above 150 horsepower
horsey['high_power'] = auto[auto.horsepower > 150].groupby('model_year').mpg.mean()
'''
            low_power  mid_power  high_power
model_year                                  
70          23.300000  18.333333   13.076923
71          26.357143  17.285714   13.333333
72          23.500000  15.000000   12.857143
73          22.166667  16.352941   12.727273
74          27.312500  15.500000         NaN
75          22.470588  17.500000   16.000000
76          25.750000  17.071429   15.500000
77          28.433333  18.100000   15.666667
78          28.363158  19.350000   17.700000
79          29.225000  20.266667   16.900000
80          34.516667  28.100000         NaN
81          31.372727  25.833333         NaN
82          32.607143  23.500000         NaN

We can see from the data here that low power cars have seen much better gains in efficiency than
mid or high power cars. I then wanted to see how much car weights have changed in that same time.
'''