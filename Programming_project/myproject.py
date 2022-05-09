import streamlit as st
from gtts import gTTS
import IPython.display as ipd  
from googletrans import Translator 
translator=Translator()
import speech_recognition as sr

#title
st.header("My Project")

#uploadfile and Speech recognition
r = sr.Recognizer()
AUDIO_FILE = "OSR_us_000_0011_8k.wav"   
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  

recognised_text= r.recognize_google(audio)

st.write('the text recognized from the audio seems to be: ')
st.write( recognised_text)
