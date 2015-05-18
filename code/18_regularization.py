###############################################################################
##### Regularization with Linear Regression
###############################################################################

## TASK: Regularized regression
## FUNCTIONS: Ridge, RidgeCV, Lasso, LassoCV
## DOCUMENTATION: http://scikit-learn.org/stable/modules/linear_model.html
## DATA: Crime (n=319 non-null, p=122, type=regression)
## DATA DICTIONARY: http://archive.ics.uci.edu/ml/datasets/Communities+and+Crime


########## Prepare data ##########
# read in data, remove categorical features, remove rows with missing values
import pandas as pd
crime = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/communities/communities.data', header=None, na_values=['?'])
crime = crime.iloc[:, 5:]
crime.dropna(inplace=True)
crime.head()

# define X and y
X = crime.iloc[:, :-1]
y = crime.iloc[:, -1]

# split into train/test
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)


########## Linear Regression Model Without Regularization ##########
# linear regression
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(X_train, y_train)
lm.coef_

# make predictions and evaluate
import numpy as np
from sklearn import metrics
preds = lm.predict(X_test)
print 'RMSE (no regularization) =', np.sqrt(metrics.mean_squared_error(y_test, preds))


########## Ridge Regression Model ##########
# ridge regression (alpha must be positive, larger means more regularization)
from sklearn.linear_model import Ridge
rreg = Ridge(alpha=0.1, normalize=True)
rreg.fit(X_train, y_train)
rreg.coef_
preds = rreg.predict(X_test)
print 'RMSE (Ridge reg.) =', np.sqrt(metrics.mean_squared_error(y_test, preds))

# use RidgeCV to select best alpha
from sklearn.linear_model import RidgeCV
alpha_range = 10.**np.arange(-2, 3)
rregcv = RidgeCV(normalize=True, scoring='mean_squared_error', alphas=alpha_range)
rregcv.fit(X_train, y_train)
rregcv.alpha_
preds = rregcv.predict(X_test)
print 'RMSE (Ridge CV reg.) =', np.sqrt(metrics.mean_squared_error(y_test, preds))

########## Lasso Regression Model ##########
# lasso (alpha must be positive, larger means more regularization)
from sklearn.linear_model import Lasso
las = Lasso(alpha=0.01, normalize=True)
las.fit(X_train, y_train)
las.coef_
preds = las.predict(X_test)
print 'RMSE (Lasso reg.) =', np.sqrt(metrics.mean_squared_error(y_test, preds))

# try a smaller alpha
las = Lasso(alpha=0.0001, normalize=True)
las.fit(X_train, y_train)
las.coef_
preds = las.predict(X_test)
print 'RMSE (Lasso reg.) =', np.sqrt(metrics.mean_squared_error(y_test, preds))

# use LassoCV to select best alpha (tries 100 alphas by default)
from sklearn.linear_model import LassoCV
lascv = LassoCV(normalize=True, alphas=alpha_range)
lascv.fit(X_train, y_train)
lascv.alpha_
lascv.coef_
preds = lascv.predict(X_test)
print 'RMSE (Lasso CV reg.) =', np.sqrt(metrics.mean_squared_error(y_test, preds))

###############################################################################
##### Regularization with Logistic Regression
###############################################################################

## TASK: Regularized classification
## FUNCTION: LogisticRegression
## DOCUMENTATION: http://scikit-learn.org/stable/modules/linear_model.html
## DATA: Titanic (n=891, p=5 selected, type=classification)
## DATA DICTIONARY: https://www.kaggle.com/c/titanic-gettingStarted/data


########## Prepare data ##########
# Get and prepare data
titanic = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT5/master/data/titanic_train.csv')
titanic['Sex'] = titanic.Sex.map({'female':0, 'male':1})
titanic.Age.fillna(titanic.Age.mean(), inplace=True)
embarked_dummies = pd.get_dummies(titanic.Embarked, prefix='Embarked').iloc[:, 1:]
titanic = pd.concat([titanic, embarked_dummies], axis=1)

# define X and y
feature_cols = ['Pclass', 'Sex', 'Age', 'Embarked_Q', 'Embarked_S']
X = titanic[feature_cols]
y = titanic.Survived

# split into train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

# standardize our data
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)


########## Logistic Regression Model Without Regularization ##########
# logistic regression
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(X_train_scaled, y_train)
logreg.coef_
y_pred = logreg.predict(X_test_scaled)

# Access accuracy
print 'Accuracy (no penalty) =', metrics.accuracy_score(y_test, y_pred)


########## Logistic Regression With L1 Penalty ##########
# logistic regression with L1 penalty (C must be positive, smaller means more regularization)
logreg_l1 = LogisticRegression(C=0.1, penalty='l1')
logreg_l1.fit(X_train_scaled, y_train)
logreg_l1.coef_
y_pred_l1 = logreg_l1.predict(X_test_scaled)

# Access accuracy
print 'Accuracy (L1 penalty) =', metrics.accuracy_score(y_test, y_pred_l1)


########## Logistic Regression With L2 Penalty ##########
# logistic regression with L2 penalty (C must be positive, smaller means more regularization)
logreg_l2 = LogisticRegression(C=0.1, penalty='l2')
logreg_l2.fit(X_train_scaled, y_train)
logreg_l2.coef_
y_pred_l2 = logreg_l2.predict(X_test_scaled)

# Access accuracy
print 'Accuracy (L2 penalty) =', metrics.accuracy_score(y_test, y_pred_l2)