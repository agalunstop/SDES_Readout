#!/usr/env python


###Modules to be imported for proper working 
import os
import Image
import pytesseract
import pyttsx
import sys
import cv2
from ImagetoText import ImagetoText
from Click import Click
from DisplayImage import DisplayImage
from ReadText import ReadText
from WikiRead import WikiRead
from ImageSearch import ImageSearch
from Meaning import Meaning

class ReadAssist(ImagetoText,Click,ReadText,ImageSearch,DisplayImage,WikiRead,Meaning):
	def __init__(self):
		Click.__init__(self)
		ImagetoText.__init__(self)
		ReadText.__init__(self)
		ImageSearch.__init__(self)
		DisplayImage.__init__(self)
		WikiRead.__init__(self)
		Meaning.__init__(self)
	def ClickPic(self):
		Click.clickphoto(self)
	def ConverttoText(self, image, fname):
		ImagetoText.ReadandWrite(self,image,fname)
	def SpeakText(self,file_name):
		ReadText.readfile(self,file_name)
	def GetImage(self,text):
		ImageSearch.imsearch(self,text)
	def ShowImage(self):
		DisplayImage.display(self)
	def GetWiki( self, text):
		WikiRead.Wiki_Function(self,text)
	def GetMeaning(self, text):
		Meaning.meaning_function(self,text)
	def __del__(self): ##destructor of class : Clean up the object and the files generated
		DisplayImage.__del__(self)
		ReadText.__del__(self)
		pass



##Test for ReadAssist




		
		

