'''
CLASS: Introduction to scikit-learn with iris data
'''

# read in iris data
import pandas as pd
col_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
iris = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',
                   names=col_names)

# create numeric column for the response
iris['species_num'] = iris.species.map({'Iris-setosa':0, 'Iris-versicolor':1, 'Iris-virginica':2})

# create X (features) two different ways
X = iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
X = iris.loc[:, 'sepal_length':'petal_width']

# create y (response)
y = iris.species_num

# predict y with KNN
from sklearn.neighbors import KNeighborsClassifier  # import class
knn = KNeighborsClassifier(n_neighbors=1)           # instantiate the estimator
knn.fit(X, y)                                       # fit with data
knn.predict([3, 5, 4, 2])                           # predict for a new observation

# predict for multiple observations at once
X_new = [[3, 5, 4, 2], [3, 5, 2, 2]]
knn.predict(X_new)

# try a different value of K
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X, y)
knn.predict(X_new)              # predictions
knn.predict_proba(X_new)        # predicted probabilities
knn.kneighbors([3, 5, 4, 2])    # distances to nearest neighbors (and identities)

# calculate Euclidian distance manually for nearest neighbor
import numpy as np
np.sqrt(((X[106] - [3, 5, 4, 2])**2).sum())
