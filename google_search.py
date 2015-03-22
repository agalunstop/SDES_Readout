##Author: Sonal Gupta & Neeraj Babu
##Python Code to extraxt out meaning of a word from google
##Can be also used to figure out other details via google search
## urllib of python, 


#!/usr/bin/python
import urllib, simplejson
 
def Search_Function(query, number,meaning):
    if meaning == 1:
        query = query + "meaning"
    query = urllib.urlencode({'q':query})
    index = number//4
    #fo=open("google_search.txt","rw+")
    if index%4!=0:index += 1 #To get more results than what user asked so that we dont fall short
    for i in xrange(0,index):
        url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&start='+str(index*4)+'&'+query
        search_results = urllib.urlopen(url)
        json = simplejson.loads(search_results.read())
        results = json['responseData']['results']
        for item in results:
            if number == 0:
                break
            print item['title'] + ": " + item['content']
          #  fo.write(['title'] + ": " + item['content'])
            number -= 1
	#fo.close()
