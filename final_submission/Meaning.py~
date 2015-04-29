##Author: Sonal Gupta & Neeraj Babu
##To get the meanings, synonyms and antonyms and translations of a word
## Required module PyDictionary of python :pip install PyDictionary


import unicodedata
import os
from PyDictionary import PyDictionary

class Meaning():
	def __init__(self):
		self.dictionary=PyDictionary()
	def meaning_function(self,query,task="mn"): #task can be meaning, translate,
		fo=open("meaning.txt","w")
		if task == "mn" :
			fo.write("Meaning :")
			fo.write(str(self.dictionary.meaning(query)))
			fo.write("Synonym :")
			fo.write(str(self.dictionary.synonym(query)))
			fo.write("Antonym :")
			fo.write(str(self.dictionary.antonym(query)))
			print (self.dictionary.meaning(query))
		elif task =="tr":
			fo.write("Translation :")
			unicodedata.normalize('NFKD', self.dictionary.translate(query,'hi')).encode('ascii','ignore')
			fo.write(unicodedata.normalize('NFKD', self.dictionary.translate(query,'hi')).encode('ascii','ignore')) ##Unicode to string conversion
			print(self.dictionary.translate(query,'hi'))
		fo.close()
	def __del__(self):
		os.remove("meaning.txt")

