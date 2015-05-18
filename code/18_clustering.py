'''
THE DATA

We have data about cars:  things like MPG, acceleration, weight, etc.  However,
we don't have logical groupings for these cars.  We can construct these 
manually using our domain knowledge (e.g. we could put all of the high mpg cars 
together and all of the low mpg cars together), but we want a more automatic
way of grouping these vehicles that can take into account more features.
'''

# Imports
from sklearn.cluster import KMeans # K means model
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Read in data
data = pd.read_table('auto_mpg.txt', sep='|') # All values range from 0 to 1
data.drop('car_name', axis=1, inplace=True) # Drop labels from dataframe
data.head()



'''
CLUSTER ANALYSIS
How do we implement a k-means clustering algorithm?

scikit-learn KMeans documentation for reference:
http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
'''

# Standardize our data
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)


# Set random seed for reproducibility 
np.random.seed(0)

# Run KMeans
est = KMeans(n_clusters=2, init='random') # Instatiate estimator
est.fit(data_scaled) # Fit your data
y_kmeans = est.predict(data_scaled) # Make cluster "predictions"

# Inspect the data by looking at the means for each cluster
data.groupby(y_kmeans).mean()

# This can be compared to the overall means for each variable
data.mean()

# We can get the coordiantes for the center of each cluster
centers = est.cluster_centers_



'''
VISUALIZING THE CLUSTERS
'''

# We can create a nice plot to visualize this upon two of the dimensions
colors = np.array(['red', 'green', 'blue', 'yellow', 'orange'])

plt.figure()
plt.scatter(data_scaled[:, 0], data_scaled[:, 5], c=colors[y_kmeans], s=50)
plt.xlabel('MPG')
plt.ylabel('Acceleration')
plt.scatter(centers[:, 0], centers[:, 5], linewidths=3, marker='+', s=300, c='black')
plt.show()

# We can generate a scatter matrix to see all of the different dimensions paired
pd.scatter_matrix(data, c=colors[y_kmeans], figsize=(15,15), s = 100)
plt.show()



'''
DETERMINING THE NUMBER OF CLUSTERS
How do you choose k? There isn't a bright line, but we can evaluate 
performance metrics such as the silhouette coefficient across values of k.

Note:  You also have to take into account practical limitations of choosing k
also.  Ten clusters may give the best value, but it might not make sense in the
context of your data.

scikit-learn Clustering metrics documentation:
http://scikit-learn.org/stable/modules/classes.html#clustering-metrics
'''

# Create a bunch of different models
k_rng = range(2,15)
k_est = [KMeans(n_clusters = k).fit(data) for k in k_rng]

# Silhouette Coefficient
# Generally want SC to be closer to 1, while also minimizing k
from sklearn import metrics
silhouette_score = [metrics.silhouette_score(data, e.labels_, metric='euclidean') for e in k_est]

# Plot the results
plt.figure()
plt.title('Silhouette coefficient for various values of k')
plt.plot(k_rng, silhouette_score, 'b*-')
plt.xlim([1,15])
plt.grid(True)
plt.ylabel('Silhouette Coefficient')
plt.show()