import streamlit as st
from googletrans import Translator 

translator=Translator()

st.header("Translator") 
word = st.text_input('Write here your word or phrase', ' ')
st.write('Your word is', word)
  
if word != 'nothing':
  lang= input('Give me a target language ')
  trans_it= translator.translate(word, dest= lang)
  st.write('the translation of this word in', trans_it.dest, 'is', trans_it.text)
else:
  st.write('you did not write any word')
