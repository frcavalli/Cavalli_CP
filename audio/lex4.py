import streamlit as st
from gtts import gTTS
import IPython.display as ipd  
from googletrans import Translator 
translator=Translator()

text= input('Write here the text: ')
lang= input('write here a 2-letter language code: ')
trans_text= translator.translate(text, dest= lang)

tts1=gTTS(trans_text.text, lang)
tts1.save("audiofile.mp3")


print('Your Audio:')
ipd.display(ipd.Audio('audiofile.mp3'))
