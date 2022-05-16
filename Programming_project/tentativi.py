import TextBlob

new_doc = TextBlob('vogio andare a casa')

result = new_doc.correct()

st.write(result)
