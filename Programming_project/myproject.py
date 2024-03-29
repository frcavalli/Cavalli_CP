import streamlit as st
from gtts import gTTS
#import IPython.display as ipd  
from googletrans import Translator 
translator=Translator()
import speech_recognition as sr


#title
st.header("Audio file translator")

urlfoto= "https://raw.githubusercontent.com/frcavalli/Cavalli_CP/main/Programming_project/immagine_progetto.jpg"
st.image(urlfoto)

st.caption('This application serves to translate an audio file into another language. Enter an audio file from your device in the box below and the application will translate it for you. The application is designed for English students trying to translate audio files into another language for study purposes, but can also be useful for tourists and people with other purposes.')
    
#uploadfile 
r = sr.Recognizer()
audio_file = st.file_uploader("Upload your audio file here")
if audio_file is not None: 
    st.audio(audio_file, format="audio/wav")
 
    st.info("Please wait. The audio transcription may take a couple of minutes!")
 #Speech recognition
    with sr.AudioFile(audio_file) as source:
         audio = r.record(source)  
        
         recognised_text= r.recognize_google(audio)
         st.subheader('The text recognized from the audio seems to be: ')
         st.write( recognised_text)
            
         st.markdown("""---""")
        #Check-spelling
         from textblob import TextBlob
         new_doc = TextBlob(recognised_text)
         st.subheader("Correction of the text")
         st.caption('I used a program to correct any errors in the transcription of the file. The corrected text looks like this: ')
         result = str(new_doc.correct())
         st.write(result)

         st.markdown("""---""")
        #Translator

         lang = st.selectbox('Choose the language in which you want to translate your text in the box below: ', ('Italian', 'Spanish', 'German', 'Croatian', 'French', 'English'))
         if lang == 'Italian':
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

         trans_text= translator.translate(result, dest= code)
         st.write('The translation of this text in ', trans_text.dest, 'is: ', trans_text.text)
        
    ttmp3=gTTS(trans_text.text, lang=code, tld='com')
    ttmp3.save("audiofile.mp3")
    my_audio= open("audiofile.mp3", "rb")
    st.write('Here is the audio of your translated text:')

    st.audio(data=my_audio, format="audio/mp3", start_time=0)
    
    st.markdown("""---""")
    st.write("Credits:")
    st.write("""
    - For the picture: https://r.search.yahoo.com/_ylt=AwrEoaa3x5RiU7gAAfgdDQx.;_ylu=c2VjA3NyBHNsawNpbWcEb2lkAzkyMTU1ZGEzYTc0MWFmNzE5Y2EyMjE5NjYxYTA4Y2I3BGdwb3MDNgRpdANiaW5n/RV=2/RE=1653946423/RO=11/RU=https%3a%2f%2fwww.diarioaveiro.pt%2fnoticia%2f24172/RK=2/RS=ZhkcC1PUMFlvopCTwoBkqSgjd8E
    """)
    st.write("""
    - For the trascription: https://docs.streamlit.io/library/api-reference/widgets/st.download_button
    """)
    st.write("""
    - For the correction of the transcription, Textblob: https://towardsdatascience.com/textblob-spelling-correction-46321fc7f8b8
    """)
    st.write("""
    - For the Audio-file: https://www.youtube.com/watch?v=TA2x8_4QNEs&t=25s
    """)
    
