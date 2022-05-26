import streamlit as st
from gtts import gTTS
import IPython.display as ipd  
from googletrans import Translator 
translator=Translator()
import speech_recognition as sr

urlfoto= "https://raw.githubusercontent.com/frcavalli/Cavalli_CP/main/Programming_project/immagine_prog_py.jpg"
st.image(urlfoto)


#title
st.header("Upload your audio file and this app will translate it for you")
st.write('This application serves to translate an audio file into another language. Enter an audio file from your device in the box below and the application will translate it for you.')
    
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
        #lang_tool = language_tool.LanguageTool("lang")
        #matches = lang_tool.check(recognised_text)
        #st.write(f'I found an error in your text that you might want to correct: ', {len(matches)})
        #len(matches)

        #Translator

         lang = st.selectbox('Choose a language: ', ('Italien', 'Spanish', 'German', 'Croatian', 'French', 'English'))
         if lang == 'Italien':
            code= 'it'
         elif lang == 'Spanish':
            code= 'es'
         elif lang == 'German':
            code= 'de'
         elif lang == 'Croatian':
            code= 'hr'
         elif lang== 'French':
            code= 'fr'
         elif lang== 'English':
            code= 'en'
       
     
         else:
            st.write('you did not write any word')

         trans_text= translator.translate(recognised_text, dest= code)
         st.write('the translation of this text in', trans_text.dest, 'is: ', trans_text.text)
        
    ttmp3=gTTS(trans_text.text, lang=code, tld='com')
    ttmp3.save("audiofile.mp3")
    my_audio= open("audiofile.mp3", "rb")
    st.write('Here is the audio of your translated text:')

    st.audio(data=my_audio, format="audio/mp3", start_time=0)

