#!/usr/env python

import ReadAssist as ReadAssist

myReader = ReadAssist()

while True:

####Wait for start

if (start = '1'):

## start processing

#Step 1: ##Capture Image

myReader.ClickPic()  #Image saved in clicked.bmp

#Step 2: ##Convert to complete text

myReader.ConverttoText("clicked.bmp", "fulltext.txt")

#Step 3: ##Extract out underline and convert to text with another name

myReader.ConverttoText("Extractedpic","underline.txt")

#Step 4: #Read from the underlined file and pass the string to a variable data as shown

with open ("underline.txt", "r") as myfile:
    data=myfile.read().replace('\n', '')

#Step 5 ##Ask for user options

## Options 

#1. Read the entire text : Call The SpeachtoText
#Exit and let the loop continnue

myReader.SpeakText("fulltext.txt")

#2. Meaning : Call the meaning function and pass data
#This function writes data to meaning.txt file
#Call SpeechtoText on this file and read out
#Exit and let the loop continnue
myReader.GetMeaning(data)
myReader.SpeakText("meaning.txt")

#3. Wiki :Call the wiki function and pass data
#This function writes data to wiki.txt file
#Call SpeechtoText on this file and read out
#Exit and let the loop continnue
myReader.GetWiki(data)
myReader.SpeakText("wiki.txt")

#4 Image : Call Image function followed by Image show
#Exit and let the loop continnue

myReader.GetImage(data)
myReader.ShowImage()

else

##Let the loop continue


#Now call 
