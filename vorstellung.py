### script for introducing our team ###

import streamlit as st
import json as js

st.title('Political Party Classification')

st.header('Erste Aufgabe: Vorstellung')

st.subheader('Unser Team')

st.text('Hallo zusammen,\nwir sind Jan Ackermann, Simon Müller und Dominik Rolof.\nWir studieren Wirtschaftsinfo und wünschen uns allen ein erfolgreiches Semester.')

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
