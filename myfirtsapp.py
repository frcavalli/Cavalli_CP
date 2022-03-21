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
