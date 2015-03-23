##Author: Sonal Gupta & Neeraj Babu
##To get the meanings, synonyms and antonyms and translations of a word
## Required module PyDictionary of python :pip install PyDictionary

#!/usr/bin/python
import unicodedata
from PyDictionary import PyDictionary
def Meaning_Function(query,task): #task can be meaning, translate,
	dictionary=PyDictionary()
	fo=open("meaning.txt","rw+")
	if task == "mn" :
		fo.write("Meaning :")
		fo.write(str(dictionary.meaning(query)))
		fo.write("Synonym :")
		fo.write(str(dictionary.synonym(query)))
		fo.write("Antonym :")
		fo.write(str(dictionary.antonym(query)))
		print (dictionary.meaning(query))
	elif task =="tr":
		fo.write("Translation :")
		unicodedata.normalize('NFKD', dictionary.translate(query,'hi')).encode('ascii','ignore')
		fo.write(unicodedata.normalize('NFKD', dictionary.translate(query,'hi')).encode('ascii','ignore')) ##Unicode to string conversion
		print(dictionary.translate(query,'hi'))
	fo.close()

