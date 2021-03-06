import streamlit as st
from PIL import Image
import json as js
import pandas as pd

st.title('Data Exploration')

st.header('Unser Datenset')

st.subheader('Auszug aus dem Twitter-Datenset')
file = open('Philipp_Amthor.jl')
data = js.load(file)

if st.button('Beispiel eines Datensatzes'):
    st.json(data)
option = st.selectbox('Möchtest du sehen, wem der Datensatz gehört?', ('Bitte auswählen...', 'Ja', 'Nein'))
if (option == 'Ja'):
    st.text('Du wolltest es nicht anders...')
    st.image('https://img-9gag-fun.9cache.com/photo/aGgXrwz_460s.jpg')
elif (option == 'Bitte auswählen...'):
    st.text('Bitte wähle Ja oder Nein')
else:
    st.text('Dann halt nicht...')

file.close()
##
if st.button('Unsere Data Preparation'):
	st.subheader('Aus 8GB .jl wird 500MB .csv ...')

	df = pd.read_csv('tweets.csv', header = None, names = ['Party', 'Tweet'])
	st.dataframe(df)

if st.button('Die meistgenutzten Wörter einzelner Parteien'):
	st.subheader('WordClouds')
	
	st.subheader('CDU - WordCloud (ungefiltert)')
	image = Image.open(str("wordclouds/CDU_wordcloud_uncleaned.png"))
	st.image(image)

	image_titles = ["CDU", "CSU", "SPD", "Die_Gruenen", "FDP", "AfD", "Die_Linke", "Fraktionslos"]

	for title in image_titles:
		st.subheader(' \n\n' + title + ' - WordCloud')
		image = Image.open(str("wordclouds/" + title + "_wordcloud.png"))
		st.image(image)
