## Class 7 Homework: Glass Identification

Let's practice what we have learned using the [Glass Identification dataset](http://archive.ics.uci.edu/ml/datasets/Glass+Identification).

1. Read the data into a DataFrame.
2. Briefly explore the data to make sure the DataFrame matches your expectations.
3. Let's convert this into a binary classification problem. Create a new DataFrame column called "binary":
    * If type of glass = 1/2/3/4, binary = 0.
    * If type of glass = 5/6/7, binary = 1.
4. Create a feature matrix "X". (Think carefully about which columns are actually features!)
5. Create a response vector "y" from the "binary" column.
6. Split X and y into training and testing sets.
7. Fit a KNN model on the training set using K=5.
8. Make predictions on the testing set and calculate accuracy.
9. Calculate the "null accuracy", which is the classification accuracy that could be achieved by always predicting the majority class.

**Bonus:**
* Write a for loop that computes the test set accuracy for a range of K values.
* Plot K versus test set accuracy to help you choose an optimal value for K.
