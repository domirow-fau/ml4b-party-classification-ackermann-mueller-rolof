# import json, os
import streamlit as st

st.header('Political Party Classification'
st.subheader('Input: Tweet -> Output: Party')

input = st.text_input('Please enter tweet...')
tweet = tweet = 'Eine Familie, die in #Niamey auf den Markt geht, muss doppelt so viel f/u00fcr einen Sack Hirse zahlen als vor einem Jahr. Zur Klimakrise kommt eine #Nahrungsmittelkrise hinzu, die Putins Angriffskrieg auf die Ukraine angeheizt hat. Wir m/u00fcssen jetzt entschlossen handeln. 2/3'

if input == tweet:
    st.text = 'Partei: Bündnis 90 - Die Grünen'



# tweetList = []

# tweet = 'Eine Familie, die in #Niamey auf den Markt geht, muss doppelt so viel f/u00fcr einen Sack Hirse zahlen als vor einem Jahr. Zur Klimakrise kommt eine #Nahrungsmittelkrise hinzu, die Putins Angriffskrieg auf die Ukraine angeheizt hat. Wir m/u00fcssen jetzt entschlossen handeln. 2/3'

# for everyFile in os.listdir("./data"):
    # file = "C:/Users/domirow/Documents/Uni/Wirtschaftsinformatik/(7) Sommersemester 2022/Machine Learning for Business/Vorlesung/example.py/data/" + everyFile
    # f = open(file)
    # print(file)
    # data = json.loads(f)
    # print(data["text"])
    # selectedTweet = data.loads("text")
    # print(everyFile)
    # if selectedTweet == tweet:
        # print("found")
    # everyFile.close()

    