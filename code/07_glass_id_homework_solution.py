'''
HOMEWORK: Glass Identification (aka "Glassification")
'''

# TASK 1: read data into a DataFrame
import pandas as pd
df = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/glass/glass.data',
                 names=['id','ri','na','mg','al','si','k','ca','ba','fe','glass_type'],
                 index_col='id')

# TASK 2: briefly explore the data
df.shape
df.head()
df.tail()
df.glass_type.value_counts()
df.isnull().sum()

# TASK 3: convert to binary classification problem (1/2/3/4 maps to 0, 5/6/7 maps to 1)
import numpy as np
df['binary'] = np.where(df.glass_type < 5, 0, 1)                        # method 1
df['binary'] = df.glass_type.map({1:0, 2:0, 3:0, 4:0, 5:1, 6:1, 7:1})   # method 2
df.binary.value_counts()

# TASK 4: create a feature matrix (X)
features = ['ri','na','mg','al','si','k','ca','ba','fe']    # create a list of features
features = df.columns[:-2]      # alternative way: slice 'columns' attribute like a list
X = df[features]                # create DataFrame X by only selecting features

# TASK 5: create a response vector (y)
y = df.binary

# TASK 6: split X and y into training and testing sets
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=99)

# TASK 7: fit a KNN model on the training set using K=5
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# TASK 8: make predictions on the testing set and calculate accuracy
y_pred = knn.predict(X_test)
from sklearn import metrics
print metrics.accuracy_score(y_test, y_pred)    # 90.7% accuracy

# TASK 9: calculate null accuracy
1 - y.mean()                                    # 76.2% null accuracy

# BONUS: write a for loop that computes test set accuracy for a range of K values
k_range = range(1, 30, 2)
scores = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    scores.append(metrics.accuracy_score(y_test, y_pred))

# BONUS: plot K versus test set accuracy to choose on optimal value for K
import matplotlib.pyplot as plt
plt.plot(k_range, scores)                       # optimal value is K=1
