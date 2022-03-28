import streamlit as st 
import json, requests
st.header("Your choice") 
title = st.text_input('write a word', 'lorem ipsum')
st.write('your word is', title)

APIkey = "914e56ce07698c06f712a3cad0747080"

url= 'https://api.datamuse.com/words?rel_rhy=' + title

