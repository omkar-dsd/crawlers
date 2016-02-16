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

bsoupFile = urllib2.urlopen("http://www.wikidata.org/wiki/Q2")
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

db = client["wiki"]

i=1
#hello = soup.find('table',{'class':'wikibase-entitytermsforlanguagelistview'})

#print hello

table = soup.find('tbody',{'class':'wikibase-entitytermsforlanguagelistview-listview'})
	#v= data.get('span class')                      #value is all href tags in a tag
	#db.coll.insert({str(i):v})               #writing in mongoDB using key,value 
# tablerows= table.find_all('tr')
trow = table.find_all("tr",{'class':'wikibase-entitytermsforlanguageview wikibase-entitytermsforlanguageview-en'})
print trow
# print tablerows
# for data in range(1,len(tablerows)):

# 	v= tablerows[data].get_text()
# 	db.coll.insert({str(i):v})

	
# 	# print (tablerows[data].get_text())
# 	# print "-------------------------------------------"
# 	i+=1


#f = tablerows[2].get_text()
#db.coll.insert({'2':f})


#db.coll.insert({"key":"val"})
#print(soup.get_text())
	