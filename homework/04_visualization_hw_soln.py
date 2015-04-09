'''
Visualization Homework Solution
'''

'''
Use the automotive mpg data (https://raw.githubusercontent.com/justmarkham/DAT5/master/data/auto_mpg.txt) 
to complete the following parts.  Please turn in your code for each part.  
Before each code chunk, give a brief description (one line) of what the code is
doing (e.g. "Loads the data" or "Creates scatter plot of mpg and weight").  If 
the code output produces a plot or answers a question, give a brief
interpretation of the output (e.g. "This plot shows X,Y,Z" or "The mean for 
group A is higher than the mean for group B which means X,Y,Z").
'''
# Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Reads text file and uses '|' as separator
auto = pd.read_table('https://raw.githubusercontent.com/justmarkham/DAT5/master/data/auto_mpg.txt', sep='|')

'''
Part 1
Produce a plot that compares the mean mpg for the different numbers of cylinders.
'''

# The first part of creating this plot is to generate the appropriate data.
# Since we want mean mpg FOR EACH number of cylinders, we should use a 'groupby'.
auto.groupby('cylinders').mpg.mean() # Give us mean mpg for each cylinder count

# Now that we have the data we want, we can think about how to plot it.
# The keyword 'compare' indiciated that you probably want to use a bar chart.
auto.groupby('cylinders').mpg.mean().plot(kind='bar') # Create plot from data
plt.title("Comparing Mean MPG for Different Numbers of Cylinders") # Add title
plt.xlabel("Number of Cylinders") # Add x label
plt.ylabel("Average MPG") # Add y label
plt.show() # Show plot
# With the exception of the three cylinder car (of which there are only 4),
# we can see that mean mpg decreases as number of cylinders increases.


'''
Part 2
Use a scatter matrix to explore relationships between different numeric variables.
'''
pd.scatter_matrix(auto) # Generate scatter matrix
pd.scatter_matrix(auto, c=auto.mpg) # Consider adding color to your scatter matrix too.
plt.show() # Show plot
'''
There are several things to notice here.  First, we can talk about different
variables' relationships with mpg.  Looking across the top row, where mpg is on
the y axis, we see that there is a clearly negative relationship between mpg 
and number of cylinders, displacement, horsepower, and weight.  There is a 
clearly positive relationship between mpg and model_year.  There is a vaguely
positive relationships between mpg and acceleration, though it's not a very 
clear one.  There also seems to be a weakly positive relationship between mpg
and origin.

There are also several other relationships you may notice:
* Dipslacement and horsepower have a positive relationship.  This makes sense,
because horsepower should increase as the engine volume (displacement) gets 
larger.
* Displacement and weight have a positive relationship.  This makes sense, 
because heavier cars tend to need bigger engines.
* Horsepower and weight have a positive relationship.  This makes sense, 
because larger cars tend to have higher horsepower engines.

There may be other inferences you could draw from this plot as well, but this 
demonstrates the usefulness of the scatter matrix in understanding your data
visually.
'''


'''
Part 3
Use a plot to answer the following questions:
'''

'''
-Do heavier or lighter cars get better mpg?
'''
# Since we want to look at the relationship between two numeric variables, we
# can use a scatterplot to see how they "move" with each other.
auto.plot(kind='scatter', x='weight', y='mpg', alpha=0.5) # Create scatter plot
plt.title('Car MPG by Weight')
plt.xlabel('Car weight')
plt.ylabel('MPG')
plt.show()
# From the plot, it appears lighter cars get better mpg.  As weight increase,
# mpg decreases.

'''
-How are horsepower and displacement related?
'''
# Once again, since we want to look at the relationship between two numeric
# variables, we can use a scatterplot.
# Notice that I didn't specify whether displacement or horsepower should be on
# the x-axis.  However, using my (limited) domain expertise, I would think that
# horsepower is affected by the displacement of the engine.  So I put 
# displacement on the x-axis and horsepower on the y-axis.
auto.plot(kind='scatter', x='displacement', y='horsepower', alpha=0.5) 
plt.title('Horsepower by Engine Displacement')
plt.xlabel('Engine Displacement')
plt.ylabel('Horsepower ')
plt.show()
# This plot shows that displacement and horsepower have a positive relationship.

'''
-What does the distribution of acceleration look like?
'''
# Since I'm interested in the distribution of acceleration, I can use a 
# histogram to investigate that.
auto.acceleration.hist()
plt.title('Distribution of Acceleration')
plt.xlabel('Acceleration')
plt.ylabel('Frequency')
plt.show()
# We can see that acceleration has an almost normal distribution.  The most 
# frequent value of acceleration is around 16.  The values of acceleration
# range from 8 to 25.

'''
-How is mpg spread for cars with different numbers of cylinders?
'''
# Since we are interested in the spread (as in the range of different values)
# for each of the different cylinder counts, we should use a boxplot as it 
# illustrates the spread of a numeric variable and accepts the "by" parameter,
# which allows us to generate a plot for each value of a variable.
auto.boxplot('mpg', by='cylinders')
plt.title('Car MPG by Number of Cylinders')
plt.xlabel('Number of Cylinders')
plt.ylabel('MPG')
plt.show()
# This plot gives us a lot of information.  I'll list a few things to notice:
# * The range for 3 cylinders is pretty small, which might be because there are
#   4 observations.
# * As shown in our earlier plots, mpg decreases as number of cylinders increases.
# * Interestingly, there are 4 cylinder cars that get relatively low gas mileage.
# * Over half of the 4 cylinder cars get better mpg than all of the 8 cylinders cars.

'''
-Do cars made before or after 1975 get better average mpg? (Hint: You need to 
create a new column that encodes whether a year is before or after 1975.)
'''
# There are several different ways to do this one.  The most straightforward 
# way could be to create a new column called 'before_1975' that contains a 
# 'Before 1975' or 'After 1975'.  We'll include 1975 in 'After 1975'.
auto['before_1975'] = np.where(auto.model_year < 75,'Before 1975', 'After 1975')
# Remember that np.where is like the IF function in Excel:
# np.where(<condition>, <value if true>, <value if false>)

# Now we can get the data we need by use a group by.
auto.groupby('before_1975').mpg.mean().plot(kind='bar')
plt.title('Average MPG Before and After 1975')
plt.xlabel('')
plt.ylabel('Average MPG')
plt.show()

# The labels are a little cut off, so you can use some extra matplotlib for 
# formatting.  'set_xticklabels' let's you set several things.
auto.groupby('before_1975').mpg.mean().plot(kind='bar').set_xticklabels(['After 1975','Before 1975'], rotation=0)
plt.title('Average MPG Before and After 1975')
plt.xlabel('')
plt.ylabel('Average MPG')
plt.show()
# We can see that the average mpg for cars after 1975 is higher.

# This could have been done without creating the extra variable.
auto.groupby(auto.model_year < 75).mpg.mean().plot(kind='bar').set_xticklabels(['After 1975','Before 1975'], rotation=0)
plt.title('Average MPG Before and After 1975')
plt.xlabel('')
plt.ylabel('Average MPG')
plt.show()
# We get the same results but without the intermediate step.