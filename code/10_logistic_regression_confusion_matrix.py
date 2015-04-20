'''
CLASS: Logistic Regression and Confusion Matrix
'''

################################################################################
### Logistic Regression
################################################################################

# imports
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics
import numpy as np

# Read in data
data = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT5/master/data/default.csv')
data.head()
# Change column to number
data['student'] = data.student.map({'No':0, 'Yes':1})

# Set X and y
feature_cols = ['student', 'balance', 'income']
X = data[feature_cols]
y = data.default
    
# Train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 2)

# Fit model
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
y_pred = logreg.predict(X_test) # Predict
print metrics.accuracy_score(y_test, y_pred)
print zip(feature_cols, logreg.coef_[0])

# Compare to null accuracy rate
y_test.mean()
1 - y_test.mean()


################################################################################
### Confusion Matrix
################################################################################

# print confusion matrix
print metrics.confusion_matrix(y_test, y_pred)

# sensitivity: percent of correct predictions when reference value is 'default'
21 / float(58 + 21)
print metrics.recall_score(y_test, y_pred)

# specificity: percent of correct predictions when reference value is 'not default'
2416 / float(2416 + 5)

# predict probabilities
import matplotlib.pyplot as plt
probs = logreg.predict_proba(X_test)[:, 1]
plt.hist(probs)
plt.show()

# use 0.5 cutoff for predicting 'default'
import numpy as np
preds = np.where(probs > 0.5, 1, 0)
print ConfusionMatrix(list(y_test), list(preds))

# change cutoff for predicting default to 0.2
preds = np.where(probs > 0.2, 1, 0)
print ConfusionMatrix(list(y_test), list(preds))

# check accuracy, sensitivity, specificity
print metrics.accuracy_score(y_test, preds)
45 / float(34 + 45)
2340 / float(2340 + 81)