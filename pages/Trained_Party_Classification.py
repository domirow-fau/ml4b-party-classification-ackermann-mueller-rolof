from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
import pandas as pd
import _pickle as cPickle
import re
import streamlit as st


st.header("Political Party Classification")
st.subheader("Vortrainierte Analyse von Tweets")
st.text("In dieser Sektion wird der Tweet\nanhand vortrainierter Modelle analysiert")

option = st.radio("Bitte gewünschte Analyse-Methode wählen:", ["Naive Bayes", "Random Forest", "Support Vector Machines"], 0)

text = st.text_input("Bitte den Tweet eingeben...", "")
text = re.sub(r'http\S+', '', text)
text = re.sub(r'\W', ' ', text)
text = re.sub(r'\s+[a-zA-Z]\s+', ' ', text)
text = re.sub(r'\^[a-zA-Z]\s+', ' ', text)
text = re.sub(r'\s+', ' ', text, flags=re.I)
text = re.sub(' RT|RT | TK|TK | amp','',text)
text = re.sub(r'^[^[a-zA-Z]]*', '', text)
text = text.lower()
text = text.strip()

if  text != "":

    df = pd.read_csv('tweets.csv')
    df = df.fillna('')
    processed_features1 = df.iloc[:,1].values
    processed_features2 = df.iloc[:,1].values
    processed_features3 = df.iloc[:,1].values
    labels = df.iloc[:, 0].values
    vectorizer1 = TfidfVectorizer (max_features=2500, min_df=7, max_df=0.8)
    vectorizer2 = TfidfVectorizer (max_features=1520, min_df=7, max_df=0.8)
    vectorizer3 = TfidfVectorizer (max_features=802, min_df=7, max_df=0.8)
    processed_features1 = vectorizer1.fit_transform(processed_features1).toarray()
    processed_features2 = vectorizer2.fit_transform(processed_features2).toarray()
    processed_features3 = vectorizer3.fit_transform(processed_features3).toarray()
    X_train, X_test, y_train, y_test = train_test_split(processed_features1, labels, test_size=0.1, random_state=0)
    X_train, X_test, y_train, y_test = train_test_split(processed_features2, labels, test_size=0.1, random_state=0)
    X_train, X_test, y_train, y_test = train_test_split(processed_features3, labels, test_size=0.1, random_state=0)

    if option == "Naive Bayes":
        print("Naive Bayes")
        st.write("Naive Bayes")
        with open('NBsave.pkl', 'rb') as fid:
            clf = cPickle.load(fid)
            #print("Partei: " + str(clf.predict(vectorizer.transform([text]))) + "\n")
            st.write("Partei: " + str(clf.predict(vectorizer1.transform([text]))))

    elif option == "Random Forest":
        print("Random Forest")
        st.write("Random Forest")
        with open('RFsave.pkl', 'rb') as fid:
            clf = cPickle.load(fid)
            #print("Partei: " + str(clf.predict(vectorizer.transform([text]))) + "\n")
            st.write("Partei: " + str(clf.predict(vectorizer2.transform([text]))))

    elif option == "Support Vector Machines":
        print("Support Vector Machines")
        st.write("Support Vector Machines")
        with open('SVMsave.pkl', 'rb') as fid:
            clf = cPickle.load(fid)
            #print("Partei: " + str(clf.predict(vectorizer.transform([text]).toarray())) + "\n")
            st.write("Partei: " + str(clf.predict(vectorizer3.transform([text]).toarray())))
            
    text = ""
