##Author: Sonal Gupta & Neeraj Babu
##Can be also used to figure out details via google search
## wikipedia module of python #pip install wikipedia


import wikipedia
import sys



class WikiRead():
	def __init__(self):
		pass

	def Wiki_Function(self,query, detail=0,tr="en"): #if detail = 0, minimum details, if 1, complete wiki page
		self.fo=open("wiki.txt","w")
		reload(sys)  # Reload does the trick!
		sys.setdefaultencoding('UTF8')
		wikipedia.set_lang("en")
		if tr == "hi":
			wikipedia.set_lang("hi")
		self.tag = wikipedia.page(query)
		if detail == 0:
			print(wikipedia.summary(query, sentences=2))
			self.fo.write(wikipedia.summary(query, sentences=2))
		elif detail == 1:
			self.fo.write(tag.content)
			print(self.tag.content)
		self.fo.close()
	def __del__self():
		os.remove("wiki.txt")


