###############################################################################
##### Class 20:  SQL
###############################################################################

"""
Accessing the data from a database is just another way to get data.  This has
no affect on how you model the data or do anything else; it's just a different
repository for storing data.  We're used to getting data from "flat files" like
CSV or TXT files.  The method for getting the data is different, but the result
is the same.
"""


###############################################################################
##### Accessing Data from a SQLLite Database
###############################################################################

# Python package to interface with database files
import sqlite3 as lite 


##### Connecting to a Database #####

# Connect to a local database (it's basically just a file)
con = lite.connect('sales.db')
con

# Create a Cursor object.  This let's you browse your database
cur = con.cursor()    
cur


##### What Tables are in our Database? ######

# Let's look at what tables we have available.  Let's not worry about what the 
# command is that it's executing.  We'll cover that more later.
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
# Note that this doesn't explicitly return anything.  It only stores the
# results in your cursor.  You have to 'fetch' the results to get them back.  
# There are several different ways to do this.  However, once you 'fetch' a 
# result, it is no longer there

# Fetch all results at once
cur.fetchall()

# One at a time
cur.fetchone()

# Some specified number at a time
cur.fetchmany(4)

# Also note that the results weren't stored anywhere, only printed out.  To 
# keep them, we must put them in a variable

cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cur.fetchall()
tables


##### Getting Data from our Database #####

# Select all of the data from the table 'Orders'
cur.execute("SELECT * FROM Orders")
orders_table = cur.fetchall()
orders_table

# This is a list of tuples, not the most convenient thing to work with, but
# managable.  We know how to access these elements.
orders_table[0]
orders_table[0][0]
orders_table[0][3]

# We could also put these into a dataframe.
import pandas as pd
orders_data = pd.DataFrame(orders_table)
orders_data

# However, pandas has a nice funtion to read the results of your SQL query into
# a pandas data frame.  This is the best thing ever!
orders_data = pd.read_sql_query("SELECT * FROM Orders", con=con)
orders_data

# Let's look at our other data to see what is contained in it.
for table in tables:
    print 'Table %s' % table[0]
    print ' '
    print pd.read_sql_query("SELECT * FROM %s" % table[0], con=con).head()
    print ' '
    print ' '
    print ' '
# NOTE: Be careful doing this if there are a lot of tables in your database.
# Here we only have five, so it's okay.

# Let's look at the sales database schema to get a better idea of the layout.
# https://raw.githubusercontent.com/justmarkham/DAT5/master/slides/20_sales_db_schema.png


###############################################################################
##### Exploring, Discovering, and Aggregating Data
###############################################################################

"""
Everything that is done in the following queries could be done in pandas.
However, it is at times easier to do it in SQL, so it's important to be aware
of how to do it.  I've included the pandas ways of doing things below the SQL 
queries for easy of comparison.
"""

##### Selecting Data #####

# Return all of the data (* means all columns)
pd.read_sql_query("SELECT * FROM Orders", con=con)
orders_data

# Return specific columns by name
pd.read_sql_query("SELECT CustomerID, EmployeeID, OrderDate, FreightCharge FROM Orders", con)
orders_data[['CustomerID','EmployeeID','OrderDate','FreightCharge']]


##### Segmenting Data #####

# Return only the more recent orders (order date more recent than 2013)
pd.read_sql_query("SELECT * FROM Orders WHERE OrderDate > '2013-01-01'", con)
orders_data[orders_data.OrderDate > '2013-01-01']

# Return only orders shipped via '1'
pd.read_sql_query("SELECT * FROM Orders WHERE ShipVia = 1", con)
orders_data[orders_data.ShipVia == 1]

# Combine conditions with AND and OR
pd.read_sql_query("SELECT * FROM Orders WHERE ShipVia = 1 AND OrderDate > '2013-01-01'", con)
orders_data[(orders_data.ShipVia == 1) & (orders_data.OrderDate > '2013-01-01')]
pd.read_sql_query("SELECT * FROM Orders WHERE ShipVia = 1 OR OrderDate > '2013-01-01'", con)
orders_data[(orders_data.ShipVia == 1) | (orders_data.OrderDate > '2013-01-01')]


##### Ordering Data #####

# We can return the rows in a specific order.
pd.read_sql_query("SELECT * FROM Orders ORDER BY OrderDate", con)
orders_data.sort_index(by="OrderDate")

# Ascending
pd.read_sql_query("SELECT * FROM Orders ORDER BY FreightCharge", con)
orders_data.sort_index(by="FreightCharge")

# Descending
pd.read_sql_query("SELECT * FROM Orders ORDER BY FreightCharge DESC", con)
orders_data.sort_index(by="FreightCharge", ascending=False)


##### Aggregating Data #####

# Count the number of rows in the order dataset
pd.read_sql_query("SELECT COUNT(*) FROM Orders", con)
orders_data.OrderID.count()
pd.read_sql_query("SELECT COUNT(*) AS row_count FROM Orders", con) # Alias column

# Compute the minimum, maximum, and average freight charge
pd.read_sql_query("""SELECT MIN(FreightCharge) AS min, MAX(FreightCharge) AS max, AVG(FreightCharge) AS avg 
                    FROM Orders""", con)
(orders_data.FreightCharge.min(), orders_data.FreightCharge.max(), orders_data.FreightCharge.mean())


##### Group By #####

# Let's look at the average freight cost by the method of shipping
# What are all of the ShipVia values?
pd.read_sql_query("SELECT DISTINCT ShipVia FROM Orders", con) # Note DISTINCT
orders_data.ShipVia.unique()

# We can write a query for each one of the ShipVia values
pd.read_sql_query("SELECT ShipVia, AVG(FreightCharge) AS avg FROM Orders WHERE ShipVia = 1", con)
orders_data[orders_data.ShipVia == 1].FreightCharge.mean()

pd.read_sql_query("SELECT ShipVia, AVG(FreightCharge) AS avg FROM Orders WHERE ShipVia = 2", con)
orders_data[orders_data.ShipVia == 2].FreightCharge.mean()

pd.read_sql_query("SELECT ShipVia, AVG(FreightCharge) AS avg FROM Orders WHERE ShipVia = 3", con)
orders_data[orders_data.ShipVia == 3].FreightCharge.mean()

pd.read_sql_query("SELECT ShipVia, AVG(FreightCharge) AS avg FROM Orders WHERE ShipVia = 4", con)
orders_data[orders_data.ShipVia == 4].FreightCharge.mean()

# However, this is pretty verbose.  Also, what if there were 20 values?  Should
# we write 20 queries?  Of course not!  This is where GROUP BY comes in.
pd.read_sql_query("SELECT ShipVia, AVG(FreightCharge) AS avg FROM Orders GROUP BY ShipVia", con)
orders_data.groupby('ShipVia').FreightCharge.mean()

# You can use any aggregation or other metric with a group by
pd.read_sql_query("SELECT ShipVia, MAX(FreightCharge) AS max FROM Orders GROUP BY ShipVia", con)
orders_data.groupby('ShipVia').FreightCharge.max()

# However, we don't know what any of these "ShipVia" values mean.  We can 
# probably look in the Shippers table and figure it out.
pd.read_sql_query("SELECT * FROM Shippers", con)
# But it's always better to have all of this info together.


###############################################################################
##### Joining Tables
###############################################################################

"""
But surely there's a better way to look at it all at once. This is where
JOIN's come in. As the name suggests, JOIN's allow you to JOIN two (or more)
tables together.  There are several types of joins:
-INNER JOIN: Returns all rows when there is at least one match in BOTH tables
-LEFT JOIN: Return all rows from the left table, and the matched rows from 
	the right table
-RIGHT JOIN: Return all rows from the right table, and the matched rows from 
	the left table
-FULL JOIN: Return all rows when there is a match in ONE of the tables

http://i.stack.imgur.com/GbJ7N.png

These have different use cases (please read more about them).  In our case, we
want to join the Shippers table (with the ShipVia ids) to the corresponding ids 
in our Orders table.  So, we want to LEFT JOIN Shippers to Orders based upon 
the matching id. 

NOTE:  You can also JOIN pandas dataframes using the "merge" function.
"""

# Let's look at the tables separately to evaluate how to join.
pd.read_sql_query("SELECT * FROM Orders", con)
pd.read_sql_query("SELECT * FROM Shippers", con)

# Let's look at the join
pd.read_sql_query("""SELECT * 
                    FROM Orders 
                    LEFT JOIN Shippers 
                    ON Orders.ShipVia = Shippers.ShipperID"""
                    , con)

# Note that any time we want to refer to a column in a particular table, we 
# have to type the table name.  That would get old.  Instead, we can give each
# table an alias or nickname.  We get the same result.
pd.read_sql_query("""SELECT * 
                    FROM Orders a 
                    LEFT JOIN Shippers b
                    ON a.ShipVia = b.ShipperID"""
                    , con)

# We can also return specific columns from each table.
pd.read_sql_query("""SELECT b.CompanyName, a.FreightCharge
                    FROM Orders a 
                    LEFT JOIN Shippers b
                    ON a.ShipVia = b.ShipperID"""
                    , con)

# We can get our result from before, but with the compnay name instead of just 
# their id.
pd.read_sql_query("""SELECT b.CompanyName, AVG(a.FreightCharge) AS avg
                    FROM Orders a 
                    LEFT JOIN Shippers b
                    ON a.ShipVia = b.ShipperID
                    GROUP BY b.CompanyName"""
                    , con)

# Finally, we can order our data by average freight charge.
pd.read_sql_query("""SELECT b.CompanyName, AVG(a.FreightCharge) AS avg
                    FROM Orders a 
                    LEFT JOIN Shippers b
                    ON a.ShipVia = b.ShipperID
                    GROUP BY b.CompanyName
                    ORDER BY avg"""
                    , con)


###############################################################################
##### Nested Queries
###############################################################################

"""
Nested queries are exactly what they sound like, queries within queries.  These
can be convenient in a number of different places.  They allow you to use the 
result from one query in another query.
"""

# Let's say we want to figure out what percentage of orders get shipped by each
# shipper.  We can count the number of occurences of each shipper.
pd.read_sql_query("SELECT ShipVia, COUNT(ShipVia) AS count FROM Orders GROUP BY ShipVia", con)

# We can calculate the number of total orders there are.
pd.read_sql_query("SELECT COUNT(*) FROM Orders", con)

# We can divide each of those by the number of orders total.
pd.read_sql_query("""SELECT ShipVia, 1.0*COUNT(ShipVia)/20*100 AS percent 
                    FROM Orders GROUP BY ShipVia""", con)

# But what happens when we get a new order.  We have to update the "20" 
# manually.  That's not optimal.  That's where nested queries help.
pd.read_sql_query("""SELECT ShipVia, 1.0*COUNT(ShipVia)/(SELECT COUNT(*) FROM Orders)*100 AS percent 
                    FROM Orders GROUP BY ShipVia""", con)

# You can nest any number of queries in a full query.


###############################################################################
##### Case Statements
###############################################################################

"""
CASE statements are similar to if else statements in Python.  They allow you to
specify conditions and what the results are if the condition is true.  They 
also allow you to specify what happens when none of the conditions are met 
(similar to the else statement in Python).
"""

# Let's say you want to determine whether the average freight charge has
# changed from year to year.  A CASE statement allows you to create conditions 
# for each year.
pd.read_sql_query("""SELECT CASE
                            WHEN OrderDate > '2012-01-01' AND OrderDate < '2013-01-01' THEN 2012
                            WHEN OrderDate > '2013-01-01' AND OrderDate < '2014-01-01' THEN 2013
                            ELSE 'Not a date!'
                            END AS year, OrderDate
                    FROM Orders""", con)

# Now we can use this to calcualte the average freight charge per year.
pd.read_sql_query("""SELECT CASE
                            WHEN OrderDate > '2012-01-01' AND OrderDate < '2013-01-01' THEN 2012
                            WHEN OrderDate > '2013-01-01' AND OrderDate < '2014-01-01' THEN 2013
                            ELSE 'Not a date!'
                            END AS year, AVG(FreightCharge) AS avg
                    FROM Orders
                    GROUP BY year""", con)
                    
# Close the connection
con.close()


###############################################################################
##### Normal Data Science Process with a Database
###############################################################################

"""
Finally, just to reiterate that getting data from databases is nothing more
than another way to get data (and thus, has no effect upon the rest of the data
science process), here is some code we used in a previous class.  Instead of 
reading data from a CSV file, we get it from a database.
"""

##### Training #####

# Open new connection
con = lite.connect('vehicles.db')

# Get training data from database
train = pd.read_sql_query('SELECT * FROM vehicle_train', con=con)

# Encode car as 0 and truck as 1
train['type'] = train.type.map({'car':0, 'truck':1})
train.head()

# Create a list of the feature columns (every column except for the 0th column)
feature_cols = train.columns[1:]

# Define X (features) and y (response)
X = train[feature_cols]
y = train.price

# Import the relevant class, and instantiate the model (with random_state=1)
from sklearn.tree import DecisionTreeRegressor
treereg = DecisionTreeRegressor(random_state=1)
treereg.fit(X, y)

# Use 3-fold cross-validation to estimate the RMSE for this model
from sklearn.cross_validation import cross_val_score
import numpy as np
scores = cross_val_score(treereg, X, y, cv=3, scoring='mean_squared_error')
np.mean(np.sqrt(-scores))


##### Testing #####

# Get testing data from database
test = pd.read_sql_query('SELECT * FROM vehicle_test', con=con)
con.close()

# Encode car as 0 and truck as 1
test['type'] = test.type.map({'car':0, 'truck':1})

# Print the data
test

# Define X and y
X_test = test[feature_cols]
y_test = test.price

# Make predictions on test data
y_pred = treereg.predict(X_test)
y_pred

# Calculate RMSE
from sklearn import metrics
np.sqrt(metrics.mean_squared_error(y_test, y_pred))

# Calculate RMSE for your own tree!
y_test = [3000, 6000, 12000]
y_pred = [3057, 3057, 16333]
np.sqrt(metrics.mean_squared_error(y_test, y_pred))