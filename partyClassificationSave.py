from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import pandas as pd
import _pickle as cPickle

df = pd.read_csv('tweets.csv', sep=',')

df = df.fillna(' ')
processed_features = df.iloc[:,1].values
labels = df.iloc[:, 0].values
vectorizer = TfidfVectorizer (max_features=2500, min_df=7, max_df=0.8)
processed_features = vectorizer.fit_transform(processed_features).toarray()
X_train, X_test, y_train, y_test = train_test_split(processed_features, labels, test_size=0.1, random_state=0)

print("Naive Bayes")
clf = MultinomialNB()
clf.fit(X_train,y_train)
predictions = clf.predict(X_test)

with open('NBsave.pkl', 'wb') as fid:
    cPickle.dump(clf, fid)

print("Random Forest")
clf = RandomForestClassifier(n_estimators=100, max_depth=60 , criterion="gini", random_state=0)
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)

with open('RFsave.pkl', 'wb') as fid:
    cPickle.dump(clf, fid)

print("Support Vector Machines")
clf = SVC()
clf.fit(X_train,y_train)
predictions = clf.predict(X_test)

with open('SVMsave.pkl', 'wb') as fid:
    cPickle.dump(clf, fid)
