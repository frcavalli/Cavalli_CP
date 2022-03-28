import streamlit as st 
import json, requests
st.header("Your choice") 
title = st.text_input('Write here your word', 'lorem ipsum')
st.write('Your word is', title)

#APIkey = "914e56ce07698c06f712a3cad0747080"

url= 'https://api.datamuse.com/words?rel_syn=' + title + '&max=5'
url1= 'https://api.datamuse.com/words?rel_ant=' + title + '&max=5'
url2= 'https://api.datamuse.com/words?sl=' + title + '&max=5'
url3= 'https://api.datamuse.com/words?ml=' + title + '&max=5'
url4= 'https://api.datamuse.com/words?sp=' + title + '&max=5'

option = st.selectbox('Which option do you want to select?', ('Synonyms', 'Antonyms', 'Sounds like', 'Means like', 'Spells like')) 
st.write('You selected:', option)

if option=='Synonyms':
  st.write(url)
elif option=='Antonyms':
  st.write(url1)
elif option=='Sounds like':
  st.write(url2)
elif option=='Means like':
  st.write(url3)
else:
  st.write(url4)
