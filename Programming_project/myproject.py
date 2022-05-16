import streamlit as st
from gtts import gTTS
import IPython.display as ipd  
from googletrans import Translator 
translator=Translator()
import speech_recognition as sr

#title
st.header("Upload your audio file and I will translate it for you")

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
   
if recognised_text != 'Nothing':
  lang= input('Give me a target language ')
  trans_it= translator.translate(recognised_text, dest= lang)
  st.write('the translation of this word/sentence in', trans_it.dest, 'is', trans_it.text)
else:
  st.write('you did not write any word/sentence')


lang = st.selectbox('Choose a 2-letter target language: ', ('italien', 'spanish', 'german', 'croatian', 'french'))
if lang == 'italien':
   code= 'it'
elif lang == 'spanish':
   code= 'es'
elif lang == 'german':
   code= 'de'
elif lang == 'croatian':
   code= 'hr'
elif lang== 'french':
   code= 'fr'
   
   trans_text= translator.translate(recognised_text, dest= code)
   st.write('the translation of this text in', trans_text.dest, 'is: ', trans_text.text)
    
   tts1=gTTS(trans_text.text, code)
   tts1.save("audiofile.mp3")
   my_audio= open("audiofile.mp3", "rb")
   st.write('Your Audio:')
    
   st.audio(data=my_audio, format="audio/mp3", start_time=0)
 
else:
   st.write('you did not write any word')
