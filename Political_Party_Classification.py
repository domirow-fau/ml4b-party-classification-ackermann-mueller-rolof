from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import pandas as pd
import re
import streamlit as st

st.set_page_config(page_title="Political Party Classification",)

st.header("Political Party Classification")
st.subheader("Analyse von Tweets")
st.text("Diese App analysiert eingegebene Tweets und sagt vorher,\nwelcher Partei der Verfasser angehört")

option = st.radio("Bitte gewünschte Analyse-Methode wählen:", ["Naive Bayes", "Random Forest", "Support Vector Machines"], 0)

n = st.slider("Bitte gewünschte Anzahl zu analysierender Tweets wählen:", 100, 15999, 100)

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
    # df = df.sample(n = 50000)
    if n > 0:
        df = df.sample(n)
    #df.drop(df.index[df.iloc[:, 0] == "A"], inplace=True)
    processed_features = df.iloc[:,1].values
    labels = df.iloc[:, 0].values
    vectorizer = TfidfVectorizer (max_features=2500, min_df=7, max_df=0.8)
    processed_features = vectorizer.fit_transform(processed_features).toarray()
    X_train, X_test, y_train, y_test = train_test_split(processed_features, labels, test_size=0.1, random_state=0)
        
    # text = "hier text ohne sonderzeichen und großbuchstaben zur vorhersage eingeben"
    if option == "Naive Bayes":
        print("Naive Bayes")
        clf = MultinomialNB()
        clf.fit(X_train,y_train)
        predictions = clf.predict(X_test)
        print("Genauigkeit: " + str(accuracy_score(y_test, predictions)))
        st.write("Genauigkeit: %.2f" % (accuracy_score(y_test, predictions) * 100) + "%")
        #print("Partei: " + str(clf.predict(vectorizer.transform([text]))) + "\n")
        st.write("Partei: " + str(clf.predict(vectorizer.transform([text]))))

    elif option == "Random Forest":
        print("Random Forest")
        clf = RandomForestClassifier(n_estimators=100, max_depth=60 , criterion="gini", random_state=0)
        clf.fit(X_train, y_train)
        predictions = clf.predict(X_test)
        print("Genauigkeit: " + str(accuracy_score(y_test, predictions)))
        st.write("Genauigkeit: %.2f" % (accuracy_score(y_test, predictions) * 100) + "%")
        #print("Partei: " + str(clf.predict(vectorizer.transform([text]))) + "\n")
        st.write(("Partei: " + str(clf.predict(vectorizer.transform([text])))))

    elif option == "Support Vector Machines":
        print("Support Vector Machines")
        clf = SVC()
        clf.fit(X_train,y_train)
        predictions = clf.predict(X_test)
        print("Genauigkeit: " + str(accuracy_score(y_test, predictions)) + "\n")
        st.write("Genauigkeit: %.2f" % (accuracy_score(y_test, predictions) * 100) + "%")
        #print("Partei: " + str(clf.predict(vectorizer.transform([text]).toarray())) + "\n")
        st.write("Partei: " + str(clf.predict(vectorizer.transform([text]).toarray())))
        
    text = ""
