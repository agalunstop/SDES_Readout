

import pyttsx
import sys

class ReadText():
	def __init__(self):
		self.engine=pyttsx.init()
	def readfile(self,file_name):
		for line in open(file_name):
    			self.engine.say(line)
		self.engine.runAndWait()
	def __del__(self):
		pass

###Test for ReadText


