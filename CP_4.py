import streamlit as st 
import json, requests
st.header("Your choice") 
title = st.text_input('Write here your word', 'lorem ipsum')
st.write('Your word is', title)


option = st.selectbox('Which option do you want to select?', ('Synonyms', 'Antonyms', 'Sounds like', 'Means like', 'Spells like')) 
st.write('You selected:', option)

url= 'https://api.datamuse.com/words?rel_syn=' + title + '&max=5'
url1= 'https://api.datamuse.com/words?rel_ant=' + title + '&max=5'
url2= 'https://api.datamuse.com/words?sl=' + title + '&max=5'
url3= 'https://api.datamuse.com/words?ml=' + title + '&max=5'
url4= 'https://api.datamuse.com/words?sp=' + title + '&max=5'

response1 = requests.get(url) 
response2 = requests.get(url1) 
response3 = requests.get(url2) 
response4 = requests.get(url3) 
response5 = requests.get(url4)   

data1 = json.loads(response1.text)
data2 = json.loads(response2.text)
data3 = json.loads(response3.text)
data4 = json.loads(response4.text)
data5 = json.loads(response5.text)


if option=='Synonyms':
  st.write(data1)
elif option=='Antonyms':
  st.write(data2)
elif option=='Sounds like':
  st.write(data3)
elif option=='Means like':
  st.write(data4)
else:
  st.write(data5)
