import streamlit as st
from PIL import Image
import json as js

st.title('Data Exploration')

st.header('Unser Datensatz')

st.subheader('Auszug aus dem Twitter-Datensatz')
file = open('Philipp_Amthor.jl')
data = js.load(file)

if st.button('Beispiel eines Datensatzes'):
    st.markdown(data)
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

st.subheader('Aus 8GB .jl wird 500MB .csv ...')

st.text('--csv einfügen--')

st.header('WordClouds')

image_titles = ["CDU", "CSU", "SPD", "Die_Gruenen", "FDP", "AfD", "Die_Linke", "Fraktionslos"]

image = Image.open("CDU_wordcloud.png"))
st.image(image)

#for title in image_titles:
#	st.subheader(' \n' + title + ' - WordCloud')
#	image = Image.open(str(title + "_wordcloud.jpeg"))
#	st.image(image)
