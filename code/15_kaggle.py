'''
CLASS: Kaggle Stack Overflow competition
'''

# read in the file and set the first column as the index
import pandas as pd
train = pd.read_csv('train.csv', index_col=0)
train.head()


'''
What are some assumptions and theories to test?

PostId: unique within the dataset
OwnerUserId: not unique within the dataset, assigned in order
OwnerCreationDate: users with older accounts have more open questions
ReputationAtPostCreation: higher reputation users have more open questions
OwnerUndeletedAnswerCountAtPostTime: users with more answers have more open questions
Tags: 1 to 5 tags are required, many unique tags
PostClosedDate: should only exist for closed questions
OpenStatus: 1 means open
'''

## OPEN STATUS

# dataset is perfectly balanced in terms of OpenStatus (not a representative sample)
train.OpenStatus.value_counts()


## USER ID

# OwnerUserId is not unique within the dataset, let's examine the top 3 users
train.OwnerUserId.value_counts()

# mostly closed questions, all lowercase, lots of spelling errors
train[train.OwnerUserId==466534]

# fewer closed questions, better grammar, high reputation but few answers
train[train.OwnerUserId==39677]

# very few closed questions, lots of answers
train[train.OwnerUserId==34537]


## REPUTATION

# ReputationAtPostCreation is higher for open questions: possibly use as a feature
train.groupby('OpenStatus').ReputationAtPostCreation.describe()

# not a useful histogram
train.ReputationAtPostCreation.hist()

# much more useful histogram
train[train.ReputationAtPostCreation < 1000].ReputationAtPostCreation.hist()

# grouped histogram
train[train.ReputationAtPostCreation < 1000].ReputationAtPostCreation.hist(by=train.OpenStatus, sharey=True)


## ANSWER COUNT

# rename column
train.rename(columns={'OwnerUndeletedAnswerCountAtPostTime':'Answers'}, inplace=True)

# Answers is higher for open questions: possibly use as a feature
train.groupby('OpenStatus').Answers.describe()

# grouped histogram
train[train.Answers < 50].Answers.hist(by=train.OpenStatus, sharey=True)


## USER ID

# OwnerUserId is assigned in numerical order
train.sort('OwnerUserId').OwnerCreationDate

# OwnerUserId is lower for open questions: possibly use as a feature
train.groupby('OpenStatus').OwnerUserId.describe()


## TITLE

# create a new feature that represents the length of the title (in characters)
train['TitleLength'] = train.Title.apply(len)

# Title is longer for open questions: possibly use as a feature
train.TitleLength.hist(by=train.OpenStatus)


## BODY

# create a new feature that represents the length of the body (in characters)
train['BodyLength'] = train.BodyMarkdown.apply(len)

# BodyMarkdown is longer for open questions: possibly use as a feature
train.BodyLength.hist(by=train.OpenStatus)


## TAGS

# Tag1 is required, and the rest are optional
train.isnull().sum()

# there are over 5000 unique tags
len(train.Tag1.unique())

# calculate the percentage of open questions for each tag
train.groupby('Tag1').OpenStatus.mean()

# percentage of open questions varies widely by tag (among popular tags)
train.groupby('Tag1').OpenStatus.agg(['mean','count']).sort('count')

# create a new feature that represents the number of tags for each question
train['NumTags'] = train.loc[:, 'Tag1':'Tag5'].notnull().sum(axis=1)

# NumTags is higher for open questions: possibly use as a feature
train.NumTags.hist(by=train.OpenStatus)


'''
Define a function that takes in a raw CSV file and returns a DataFrame that
includes all created features (and any other modifications). That way, we
can apply the same changes to both train.csv and test.csv.
'''

# define the function
def make_features(filename):
    df = pd.read_csv(filename, index_col=0)
    df.rename(columns={'OwnerUndeletedAnswerCountAtPostTime':'Answers'}, inplace=True)
    df['TitleLength'] = df.Title.apply(len)
    df['BodyLength'] = df.BodyMarkdown.apply(len)
    df['NumTags'] = df.loc[:, 'Tag1':'Tag5'].notnull().sum(axis=1)
    return df

# apply function to both training and testing files
train = make_features('train.csv')
test = make_features('test.csv')


'''
Use train/test split to compare a model that includes 1 feature with a model
that includes 5 features.
'''

## ONE FEATURE

# define X and y
feature_cols = ['ReputationAtPostCreation']
X = train[feature_cols]
y = train.OpenStatus

# split into training and testing sets
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

# fit a logistic regression model
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(X_train, y_train)

# examine the coefficient to check that it makes sense
logreg.coef_

# predict response classes and predict class probabilities
y_pred = logreg.predict(X_test)
y_prob = logreg.predict_proba(X_test)[:, 1]

# check how well we did
from sklearn import metrics
metrics.accuracy_score(y_test, y_pred)      # 0.538 (better than guessing)
metrics.confusion_matrix(y_test, y_pred)    # predicts closed most of the time
metrics.roc_auc_score(y_test, y_prob)       # 0.602 (not horrible)
metrics.log_loss(y_test, y_prob)            # 0.690 (what is this?)

# log loss is the competition's evaluation metric, so let's get a feel for it
true = [0, 0, 1, 1]
prob = [0.1, 0.2, 0.8, 0.9]
metrics.log_loss(true, prob)        # 0.164 (lower is better)

# let's try a few other predicted probabilities and check the log loss
prob = [0.4, 0.4, 0.6, 0.6]         # 0.511 (predictions are right, but less confident)
prob = [0.4, 0.4, 0.4, 0.6]         # 0.612 (one wrong prediction that is a bit off)
prob = [0.4, 0.4, 0.1, 0.6]         # 0.959 (one wrong prediction that is way off)
prob = [0.5, 0.5, 0.5, 0.5]         # 0.693 (you can get this score without a model)


## FIVE FEATURES

# define X and y
feature_cols = ['ReputationAtPostCreation', 'Answers', 'TitleLength', 'BodyLength', 'NumTags']
X = train[feature_cols]
y = train.OpenStatus

# split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

# fit a logistic regression model
logreg.fit(X_train, y_train)

# examine the coefficients to check that they make sense
logreg.coef_

# predict response classes and predict class probabilities
y_pred = logreg.predict(X_test)
y_prob = logreg.predict_proba(X_test)[:, 1]

# check how well we did
metrics.accuracy_score(y_test, y_pred)      # 0.589 (doing better)
metrics.confusion_matrix(y_test, y_pred)    # predicts open more often
metrics.roc_auc_score(y_test, y_prob)       # 0.625 (tiny bit better)
metrics.log_loss(y_test, y_prob)            # 0.677 (a bit better)

# let's see if cross-validation gives us similar results
from sklearn.cross_validation import cross_val_score
scores = cross_val_score(logreg, X, y, scoring='log_loss', cv=10)
scores.mean()       # 0.677 (identical to train/test split)
scores.std()        # very small


'''
Use the model with 5 features to make a submission
'''

# make sure that X and y are defined properly
feature_cols = ['ReputationAtPostCreation', 'Answers', 'TitleLength', 'BodyLength', 'NumTags']
X = train[feature_cols]
y = train.OpenStatus

# train the model on ALL data (not X_train and y_train)
logreg.fit(X, y)

# predict class probabilities for the actual testing data (not X_test)
y_prob = logreg.predict_proba(test[feature_cols])[:, 1]

# sample submission file indicates we need two columns: PostId and predicted probability
test.index      # PostId
y_prob          # predicted probability

# create a DataFrame that has 'id' as the index, then export to a CSV file
sub = pd.DataFrame({'id':test.index, 'OpenStatus':y_prob}).set_index('id')
sub.to_csv('sub1.csv')


'''
Create a few more features from Title
'''

# string methods for a Series are accessed via 'str'
train.Title.str.lower()

# create a new feature that represents whether a Title is all lowercase
train['TitleLowercase'] = (train.Title.str.lower() == train.Title).astype(int)

# check if there are a meaningful number of ones
train.TitleLowercase.value_counts()

# percentage of open questions is lower among questions with lowercase titles: possibly use as a feature
train.groupby('TitleLowercase').OpenStatus.mean()

# create features that represent whether Title contains certain words
train['TitleQuestion'] = train.Title.str.contains('question', case=False).astype(int)
train['TitleNeed'] = train.Title.str.contains('need', case=False).astype(int)
train['TitleHelp'] = train.Title.str.contains('help', case=False).astype(int)


'''
Build a document-term matrix from Title using CountVectorizer
'''

# define X and y
X = train.Title
y = train.OpenStatus

# split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

# use CountVectorizer with the default settings
from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer()

# fit and transform on X_train, but only transform on X_test
train_dtm = vect.fit_transform(X_train)
test_dtm = vect.transform(X_test)

# try a Naive Bayes model
from sklearn.naive_bayes import MultinomialNB
nb = MultinomialNB()
nb.fit(train_dtm, y_train)
y_prob = nb.predict_proba(test_dtm)[:, 1]
metrics.log_loss(y_test, y_prob)            # 0.659 (a bit better than our previous model)

# try tuning CountVectorizer and repeat Naive Bayes
vect = CountVectorizer(stop_words='english')
train_dtm = vect.fit_transform(X_train)
test_dtm = vect.transform(X_test)
nb.fit(train_dtm, y_train)
y_prob = nb.predict_proba(test_dtm)[:, 1]
metrics.log_loss(y_test, y_prob)            # 0.637 (even better)

# try switching to logistic regression
logreg.fit(train_dtm, y_train)
y_prob = logreg.predict_proba(test_dtm)[:, 1]
metrics.log_loss(y_test, y_prob)            # 0.573 (much better!)


'''
Create features from BodyMarkdown using TextBlob
'''

# examine BodyMarkdown for first question
train.iloc[0].BodyMarkdown

# calculate the number of sentences in that question using TextBlob
from textblob import TextBlob
len(TextBlob(train.iloc[0].BodyMarkdown).sentences)

# calculate the number of sentences for all questions (raises an error)
train.BodyMarkdown.apply(lambda x: len(TextBlob(x).sentences))

# explicitly decode string to unicode to fix error (WARNING: VERY SLOW)
train['BodySentences'] = train.BodyMarkdown.apply(lambda x: len(TextBlob(x.decode('utf-8')).sentences))
