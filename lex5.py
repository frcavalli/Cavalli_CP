from googletrans import Translator 

translator=Translator()

st.header("Translator") 
title = st.text_input('Write here your word', 'lorem ipsum')
st.write('Your word is', title)


while True:
  word= input('Give me a word or a phrase ')
  
  if word != 'nothing':
    lang= input('Give me a target language ')
    trans_it= translator.translate(word, dest= lang)
    print('the translation of this word in', trans_it.dest, 'is', trans_it.text)
  else:
    print('you did not write any word')
    break
