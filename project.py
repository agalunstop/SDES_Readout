###Python Project######
####Authors: Sonal Gupta & Neeraj Babu
###This program takes pictures of hardcopy of documents/pages of books and so on
###extracts text from them, searches for a particular string from the extracted 

import Image
import pytesseract
import pyttsx
import sys
#import cv2
##for cv2 import *
###Code for acquiring image from camera




###Code_Segment2##OCR_Neeraj
#####Opening the image and extracting text and dumping it to myfile.txt
fo=open("myfile.txt","w")
fo.write(pytesseract.image_to_string(Image.open(sys.argv[1])))
fo.close()


####Code_Segment2## Text read out


#engine = pyttsx.init()
#for line in open("myfile.txt"):
#    engine.say(line)
#engine.runAndWait()
