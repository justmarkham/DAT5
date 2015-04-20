'''
CLASS: Logistic Regression and Confusion Matrix
'''

###############################################################################
### Logistic Regression
###############################################################################

# Imports
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from math import exp
import numpy as np
import matplotlib.pyplot as plt

# Read in data
data = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT5/master/data/default.csv')
data.head()
# Change column to number
data['student_bin'] = data.student.map({'No':0, 'Yes':1})

# Let's do some cursory analysis.
data.groupby('default').balance.mean()
data.groupby('default').income.mean()

# Set X and y
feature_cols = ['balance', 'income','student_bin']
X = data[feature_cols]
y = data.default
    
# Train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 2)

# Fit model
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
y_pred = logreg.predict(X_test) # Predict

# Access accuracy
print metrics.accuracy_score(y_test, y_pred)


###############################################################################
### Null Accuracy Rate
###############################################################################

# Compare to null accuracy rate. The null accuracy rate is the accuracy if I 
# predict all the majority class.  If there are more 1's, I predict all 1's.  
# If there are more 0's, I predict all 0's. There are several ways to do this.

# 1. Create a vector of majority class and use the accuracy_score.
# "If I predicted all 0's, how accurate would I be?
print metrics.accuracy_score(y_test, [0]*len(y_pred))

# 2. Calculate the mean of y_test (AKA the percentage of 1's)
y_test.mean()
# One minus that number will be the percentage of 0's.  This means that if you 
# predict all 0's, you will be correct 1-y_test-mean() percent of the time.
1 - y_test.mean()

# This puts our accuracy score into context a bit.  We can now see that we 
# actually didn't do so great!


###############################################################################
### Intepretting Logistic Regression Coefficients
###############################################################################

# Let's look at the coefficients
for col in zip(feature_cols, logreg.coef_[0]):
    print col[0], col[1]
    
# Let's interpret those.
for col in zip(feature_cols, logreg.coef_[0]):
    print 'A unit increase in', col[0], 'equals a', exp(col[1]), 'increase in odds.'

###############################################################################
### Confusion Matrix
###############################################################################

# Let's look at the confusion matrix
con_mat = metrics.confusion_matrix(y_test, y_pred)
print con_mat

# Let's define our true posititves, false positives, true negatives, and false negatives
true_neg = con_mat[0][0]
false_neg = con_mat[1][0]
true_pos = con_mat[1][1]
false_pos = con_mat[0][1]

# Sensitivity: percent of correct predictions when reference value is 'default'
sensitivity = float(true_pos)/(false_neg + true_pos)
print sensitivity
print metrics.recall_score(y_test, y_pred)

# Specificity: percent of correct predictions when reference value is 'not default'
specificity = float(true_neg) / (true_neg + false_pos)
print specificity

###############################################################################
### Logistic Regression Thresholds
###############################################################################

# Logistic regression is actually predicting the underlying probability.  
# However, when you clal the "predict" function, it returns class labels.  You
# can still predict the actual probability and set your own threshold if you'd
# like.  This can be useful in cases where the "signal" from the model isn't 
# strong.

# Predict probabilities
logreg.predict_proba(X_test)
probs = logreg.predict_proba(X_test)[:, 1]

# The natural threshold for probabilility is 0.5, but you don't have to use 
# that.

# Use 0.5 thrshold for predicting 'default' and confirm we get the same results
preds_05 = np.where(probs >= 0.5, 1, 0)
print metrics.accuracy_score(y_test, preds_05)
con_mat_05 = metrics.confusion_matrix(list(y_test), list(preds_05))
print con_mat_05

# Let's look at a histogram of these probabilities.
plt.hist(probs, bins=20)
plt.title('Distribution of Probabilities')
plt.xlabel('Probability')
plt.ylabel('Frequency')
plt.show()

# Change cutoff for predicting default to 0.2
preds_02 = np.where(probs > 0.2, 1, 0)
delta = float((preds_02 != preds_05).sum())/len(X_test)*100
print 'Changing the threshold from 0.5 to 0.2 change %.2f percent of the predictions.' % delta

# Check the new accuracy, sensitivity, specificity
print metrics.accuracy_score(y_test, preds_02)
con_mat_02 = metrics.confusion_matrix(list(y_test), list(preds_02))
print con_mat_02

# Let's define our true posititves, false positives, true negatives, and false negatives
true_neg = con_mat_02[0][0]
false_neg = con_mat_02[1][0]
true_pos = con_mat_02[1][1]
false_pos = con_mat_02[0][1]

# Sensitivity: percent of correct predictions when reference value is 'default'
sensitivity = float(true_pos)/(false_neg + true_pos)
print sensitivity
print metrics.recall_score(y_test, preds_02)

# Specificity: percent of correct predictions when reference value is 'not default'
specificity = float(true_neg) / (true_neg + false_pos)
print specificity


###############################################################################
### Exercise/Possibly Homework
###############################################################################

'''
Let's use the glass identification dataset again.   We've previously run knn
on this dataset.  Now, let's try logistic regression.  Access the dataset at
http://archive.ics.uci.edu/ml/datasets/Glass+Identification.  Complete the 
following tasks or answer the following questions.

1. Read the data into a pandas dataframe.
2. Explore the data and look at what columns are available.
3. Convert the 'glass type' column into a binary response.
    * If type of class = 1/2/3/4, binary=0.
    * If type of glass = 5/6/7, binary=1.
4. Create a feature matrix and a response vector.  
5. Split the data into the appropriate training and testing sets.
6. Create and fit a logistic regression model.
7. Make predictions with your new model.
8. Calculate the accuracy rate of your model and compare it to the null accuracy.
9. Generate a confusion matrix for your predictions.  Use this to calculate the
sensitivity and specificity of your model.
'''