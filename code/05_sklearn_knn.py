'''
CLASS: Introduction to scikit-learn with iris data
'''

# read in iris data
import pandas as pd
col_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
iris = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',
                   names=col_names)

# create numeric column for the response
# note: features and response must both be entirely numeric!
iris['species_num'] = iris.species.map({'Iris-setosa':0, 'Iris-versicolor':1, 'Iris-virginica':2})

# create X (features) three different ways
X = iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
X = iris.loc[:, 'sepal_length':'petal_width']
X = iris.iloc[:, 0:4]

# create y (response)
y = iris.species_num

# check the shape of X and y
X.shape     # 150 by 4 (n=150, p=4)
y.shape     # 150 (must match first dimension of X)

# scikit-learn 4-step modeling pattern:

# Step 1: import the class you plan to use
from sklearn.neighbors import KNeighborsClassifier

# Step 2: instantiate the "estimator" (aka the model)
# note: all unspecified parameters are set to the defaults
knn = KNeighborsClassifier(n_neighbors=1)

# Step 3: fit the model with data (learn the relationship between X and y)
knn.fit(X, y)

# Step 4: use the "fitted model" to predict the response for a new observation
knn.predict([3, 5, 4, 2])

# predict for multiple observations at once
X_new = [[3, 5, 4, 2], [3, 5, 2, 2]]
knn.predict(X_new)

# try a different value of K ("tuning parameter")
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X, y)
knn.predict(X_new)              # predicted classes
knn.predict_proba(X_new)        # predicted probabilities of class membership
knn.kneighbors([3, 5, 4, 2])    # distances to nearest neighbors (and identities)

# calculate Euclidian distance manually for nearest neighbor
import numpy as np
np.sqrt(((X.iloc[106, :] - [3, 5, 4, 2])**2).sum())
