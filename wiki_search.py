##Author: Sonal Gupta & Neeraj Babu
##Can be also used to figure out details via google search
## wikipedia module of python #pip install wikipedia

#!/usr/bin/python
import wikipedia
def Wiki_Function(query, detail,tr): #if detail = 0, minimum details, if 1, complete wiki page
	fo=open("wiki.txt","rw+")
	wikipedia.set_lang("en")
	if tr == "hi":
		wikipedia.set_lang("hi")
	tag = wikipedia.page(query)
	if detail == 0:
		print(wikipedia.summary(query, sentences=2))
	#	fo.write(wikipedia.summary(query, sentences=2))
	elif detail == 1:
	#	fo.write(tag.content)
		print(tag.content)
	fo.close()
