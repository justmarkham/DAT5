'''
Imports
'''
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import make_pipeline


'''
Define a function that takes in a raw CSV file and returns a DataFrame that
includes all created features (and any other modifications). That way, we
can apply the same changes to both train.csv and test.csv.
'''

# Define the function
def make_features(filename):
    # Read in dataframe    
    df = pd.read_csv(filename, index_col=0)
    
    #Rename columns 
    df.rename(columns={'OwnerUndeletedAnswerCountAtPostTime':'Answers'}, inplace=True)

    # Get length of title of post    
    df['TitleLength'] = df.Title.apply(len)
    
    # Get length of body of post
    df['BodyLength'] = df.BodyMarkdown.apply(len)
    
    # Number of tags for post
    df['NumTags'] = df.loc[:, 'Tag1':'Tag5'].notnull().sum(axis=1)
    
    # Is the title lowercase?
    df['TitleLowercase'] = (df.Title.str.lower() == df.Title).astype(int)
    
    # Create features that represent whether Title contains certain words
    df['TitleQuestion'] = df.Title.str.contains('question', case=False).astype(int)
    df['TitleNeed'] = df.Title.str.contains('need', case=False).astype(int)
    df['TitleHelp'] = df.Title.str.contains('help', case=False).astype(int)

    return df

# Apply function to the training data
train = make_features('train.csv')
X = train.drop('OpenStatus', axis=1)
y = train.OpenStatus

# Read in test data
test = make_features('test.csv')


# Split into training and testing sets
#X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

'''
Five feature logistic regression model
'''
# Define feature cols
feature_cols_logreg = ['ReputationAtPostCreation', 'Answers', 'TitleLength', 'BodyLength', 'NumTags']

# Perform cross validation to get an idea of the performance of the model
logreg = LogisticRegression()
-cross_val_score(logreg, X[feature_cols_logreg], y, scoring="log_loss", cv=5).mean()

# Predict class probabilities for the actual testing data
logreg.fit(X[feature_cols_logreg], y)
y_prob_logreg = logreg.predict_proba(test[feature_cols_logreg])[:, 1]

'''
Five feature random forest model
'''
# Define feature cols
feature_cols_rf = ['TitleLowercase', 'TitleQuestion', 'TitleNeed', 'TitleHelp']

# Perform cross validation to get an idea of the performance of the model
rf = RandomForestClassifier()
-cross_val_score(rf, X[feature_cols_rf], y, scoring="log_loss", cv=5).mean()

# Predict class probabilities for the actual testing data
rf.fit(X[feature_cols_rf], y)
y_prob_rf = rf.predict_proba(test[feature_cols_rf])[:, 1]



'''
Text logistic regression model on 'Title' using pipeline
'''

# Make pipleline
pipe = make_pipeline(CountVectorizer(stop_words='english'), LogisticRegression())

# Perform cross validation to get an idea of the performance of the model
-cross_val_score(pipe, X['Title'], y, scoring="log_loss", cv=5).mean()

# Predict class probabilities for the actual testing data
pipe.fit(X['Title'], y)
y_prob_pipe = pipe.predict_proba(test['Title'])[:, 1]


'''
Create submission
'''
# Ensemble predictions
y_prob_combined = (y_prob_logreg + y_prob_rf + 2*y_prob_pipe) / 3

# Create a DataFrame that has 'id' as the index, then export to a CSV file
sub = pd.DataFrame({'id':test.index, 'OpenStatus':y_prob_combined}).set_index('id')
sub.to_csv('sub_ensemble.csv')
