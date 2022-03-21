# Cavalli_CP
import streamlit as st 
import json, requests
st.header("hello world") 
title = st.text_input('Gimme a movie title', 'lorem ipsum')
st.write('The current movie title is', title)





 # ! python3
 

# add your own APIkey
APIkey = "914e56ce07698c06f712a3cad0747080"
location = st.text_input("Give me the name of a city")

# check API documentation to see what structure of URL is needed to access the data
# http://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
url = 'http://api.openweathermap.org/data/2.5/weather?q=' + location + '&appid=' + APIkey
# print(url)


# Download the JSON data from OpenWeatherMap.org's API.
response = requests.get(url)  
# Uncomment to see the raw JSON text:
# print(response.text)  


# Load JSON data into a Python variable.
weatherData = json.loads(response.text)
# Uncomment to see the raw JSON text:
st.write(weatherData) 
# from pprint import pprint 
# pprint(weatherData) 

st.write(weatherData['main']['temp_max']) 

location = st.radio("Give me a city name",('Rome', 'Verona', 'Miland'))
if location == 'Rome':
    st.write('You selected Rome')
    st.write(weatherData)
if location == 'Verona':
    st.write("You selected Verona")
    st.write(weatherData)
else:
    st.write("You selected Miland")
    st.write(weatherData)
