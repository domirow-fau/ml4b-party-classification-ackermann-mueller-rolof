from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
import pandas as pd
import _pickle as cPickle
import streamlit as st

text = "test"

df = pd.read_csv('tweets.csv')
df = df.fillna('')
processed_features = df.iloc[:,1].values
labels = df.iloc[:, 0].values
vectorizer = TfidfVectorizer (max_features=2500, min_df=7, max_df=0.8)
processed_features = vectorizer.fit_transform(processed_features).toarray()
X_train, X_test, y_train, y_test = train_test_split(processed_features, labels, test_size=0.1, random_state=0)

st.write("Naive Bayes")
with open('NBsave.pkl', 'rb') as fid:
    clf = cPickle.load(fid)
    st.write("Partei: " + str(clf.predict(vectorizer.transform([text]))))
    
vectorizer = TfidfVectorizer (max_features=1520, min_df=7, max_df=0.8)
processed_features = vectorizer.fit_transform(processed_features).toarray()
X_train, X_test, y_train, y_test = train_test_split(processed_features, labels, test_size=0.1, random_state=0)

st.write("Random Forest")
with open('RFsave.pkl', 'rb') as fid:
    clf = cPickle.load(fid)
    st.write("Partei: " + str(clf.predict(vectorizer.transform([text]))))

st.write("Support Vector Machines")
with open('SVMsave.pkl', 'rb') as fid:
    clf = cPickle.load(fid)
    st.write("Partei: " + str(clf.predict(vectorizer.transform([text]).toarray())))
