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
audio_file = st.file_uploader("Upload your audio file here")
if audio_file is not None: 
    coll_data= audio_file.getvalue()
    st.write(coll_data)
    
    stringio=StringIO(audio_file.getvalue().decode("utf-8"))
    st.write(stringio)
     
    new_string = stringio.read()
    st.write(new_string)
    
    dataframe = pd.read_csv(audio_file)
    st.write(dataframe)
    
    
with sr.audiofile(audio_file) as source:
    audio = r.record(source)  

recognised_text= r.recognize_google(audio)

st.write('the text recognized from the audio seems to be: ')
st.write( recognised_text)


