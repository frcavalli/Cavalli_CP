# Cavalli_CP
import streamlit as st
st.header("hello world") 
title = st.text_input('Gimme a movie title', 'lorem ipsum')
st.write('The current movie title is', title)

import streamlit as st
genre = st.radio("What's your favorite movie genre",('Comedy', 'Drama', 'Documentary'))
if genre == 'Comedy':
    st.write('You selected comedy.')
else:
    st.write("You didn't select comedy.")

  # ! python3
import json, requests 

# add your own APIkey
APIkey = "914e56ce07698c06f712a3cad0747080"
location = "London" 
# st.text_input("Give me the name of a city")

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
#print(weatherData) 
# from pprint import pprint 
# pprint(weatherData) 

st.write(weatherData['main']['temp_max']) 

-----------------------------------------------------------------------------

 # ! python3
import json, requests 

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
