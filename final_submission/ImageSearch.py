

import os
import sys
import time
from urllib import FancyURLopener
import urllib2
import simplejson



# Start FancyURLopener with defined version 
class MyOpener(FancyURLopener): 
    version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'


#Class for reteriving images as per the search term
class ImageSearch():
	def __init__(self):
		pass
	def imsearch(self,search_text):
		self.searchTerm = search_text
		# Replace spaces ' ' in search term for '%20' in order to comply with request
		self.searchTerm = self.searchTerm.replace(' ','%20')
		self.myopener = MyOpener()

		# Set count to 0
		self.count= 0

		for self.i in range(0,1):
   		 #start changes for each iteration in order to request a new set of images for each loop
    			self.url = ('https://ajax.googleapis.com/ajax/services/search/images?' + 					'v=1.0&q='+self.searchTerm+'&start='+str(self.i*4)+'&userip=MyIP')
    			print self.url
    			self.request = urllib2.Request(self.url, None, {'Referer': 'testing'})
    			self.response = urllib2.urlopen(self.request)

   		 # Getting results using JSON
    			self.results = simplejson.load(self.response)
    			self.data = self.results['responseData']
    			self.dataInfo = self.data['results']

  		# Iterate for each result and get unescaped url
  			for self.myUrl in self.dataInfo:
        			self.count = self.count + 1
       				print self.myUrl['unescapedUrl']
				self.myopener.retrieve(self.myUrl['unescapedUrl'],str(self.count)+'.jpg')

    # Sleep for one second to prevent IP blocking from Google
    	time.sleep(1)
	def _del__(self):
		pass
		
