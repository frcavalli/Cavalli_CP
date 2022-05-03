import streamlit as st
from gtts import gTTS
import IPython.display as ipd  
from googletrans import Translator 

translator=Translator()

st.header("Translator and Audio-file")

text= st.text_input('Write here the text you want to translate: ')
code= ''
if text != '':
  st.write('Your text is: ', text)
  if text != '':
    lang = st.selectbox('Choose a 2-letter target language: ', ('italien', 'spanish', 'german', 'croatian', 'french', 'russian',))
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
    elif lang== 'russian':
      code= 'ru'
   
    trans_text= translator.translate(text, dest= code)
    st.write('the translation of this text in', trans_text.dest, 'is: ', trans_text.text)
    
    tts1=gTTS(trans_text.text, code)
    tts1.save("audiofile.mp3")
    my_audio= open("audiofile.mp3", "rb")
    st.write('Your Audio:')
    
    st.audio(data=my_audio, format="audio/mp3", start_time=0)
    
    #st.audio(ipd.display(ipd.Audio('audiofile.mp3')))
    
  else:
    st.write('you did not write any word')




