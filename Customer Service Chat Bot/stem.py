import nltk #natural language tool kit library 
from nltk.stem import LancasterStemmer #import the module to stem the words 

stemmer = LancasterStemmer() #asssign the module to the stem placehlder 

words = ['throwing', 'scammed', 'jumping']
stemmed_word =  [stemmer.stem(word) for word in words]
print(stemmed_word)
