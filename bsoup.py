from pymongo import MongoClient


from bs4 import BeautifulSoup
import urllib2

#url = "http://www.pythonforbeginners.com"			
#content = urllib2.urlopen(url).read()

#----- PROXY HANDLER -------
proxy=urllib2.ProxyHandler({})
opener=urllib2.build_opener(proxy)
opener.addheaders=[('User-agent','Mozilla/5.0')]
urllib2.install_opener(opener)
#----- END PROXY HANDLER ------

bsoupFile = urllib2.urlopen("http://www.reddit.com")
bsoupHtml = bsoupFile.read()

#bsoupFile.close()

soup = BeautifulSoup(bsoupHtml)

#print soup.prettify()


#title = soup.find_all("title")  #title tag stored into object

#print "TITLEEEEEEEEE :::::::: ", title
#print "------TITLE ENDS HERE------"

#print soup.title.string
#print soup.meta

client = MongoClient()

db = client["test"]

i=1
for link in soup.find_all('a'):
	v= link.get('href')								#value is all href tags in a tag
	db.coll.insert({str(i):v})						#writing in mongoDB using key,value 
	print (link.get('href'))	
	print "-------------------------------------------"
	i+=1

#db.coll.insert({"key":"val"})
#print(soup.get_text())
