import streamlit as st
from gtts import gTTS
import IPython.display as ipd  
from googletrans import Translator 

translator=Translator()

st.header("Translator")

text= st.input('Write here the text you want to translate: ', ' ')

if text != ' ':
  st.write('Your text is: ', text)
  if text != 'nothing':
    lang= st.text_input('Give me a 2-letter target language ', 'en')
    trans_text= translator.translate(text, dest= lang)
    st.write('the translation of this text in', trans_text.dest, 'is: ', trans_text.text)
    
    tts1=gTTS(trans_text.text, lang)
    tts1.save("audiofile.mp3")
    my_audio= open("audiofile.mp3", "rb")
    st.write('Your Audio:')
    
    st.audio(data=audio_file, format="audio/mp3", start_time=0)
    
    #st.audio(ipd.display(ipd.Audio('audiofile.mp3')))
    
  else:
    st.write('you did not write any word')



