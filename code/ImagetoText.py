##Authors: Neeraj Babu & Sonal Gupta
## TDD for Tesseract OCR


import Image
import pytesseract
import sys

class ImagetoText():
	def __init__(self):
		pass
	def ReadandWrite(self,image,text):
		self.text=text
		self.image=image
		self.fo=open(self.text,"w")
		self.fo.write(pytesseract.\
			image_to_string(Image.open(self.image)))
		self.fo.close()
	def __del__(self):
		os.remove(self.text)
		pass

