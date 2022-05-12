import streamlit as st
from gtts import gTTS
import IPython.display as ipd  
from googletrans import Translator 
translator=Translator()
import speech_recognition as sr

#title
st.header("My Project")

#uploadfile 
r = sr.Recognizer()
audio_file = st.file_uploader("Upload your audio file here")
if audio_file is not None: 
    st.audio(audio_file, format="audio/wav")
    
    #Speech recognition
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)  

    recognised_text= r.recognize_google(audio)

    st.write('The text recognized from the audio seems to be: ')
    st.write( recognised_text)

    
#Check-spelling 


#Translator
   
if recognised_text != 'nothing':
  lang= input('Give me a target language ')
  trans_it= translator.translate(recognised_text, dest= lang)
  st.write('the translation of this word/sentence in', trans_it.dest, 'is', trans_it.text)
else:
  st.write('you did not write any word/sentence')
