import streamlit as st 
import json, requests
st.header("Your choice") 
title = st.text_input('Write here your word', 'lorem ipsum')
st.write('Your word is', title)

#APIkey = "914e56ce07698c06f712a3cad0747080"

url= 'https://api.datamuse.com/words?rel_rhy=' + title + '&max=5'

option = st.selectbox('Which option do you want to select?', ('Synonyms', 'Antonyms', 'Sounds like' 'Means like')) 
st.write('You selected:', option)
