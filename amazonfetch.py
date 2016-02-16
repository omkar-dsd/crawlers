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

bsoupFile = urllib2.urlopen("http://www.amazon.com/s/ref=nb_sb_noss_2/185-5945162-0333204?url=search-alias%3Daps&field-keywords=laptop")
bsoupHtml = bsoupFile.read()

#bsoupFile.close()

soup = BeautifulSoup(bsoupHtml)

#print soup.prettify()


#title = soup.find_all("title")  #title tag stored into object

#print "TITLEEEEEEEEE :::::::: ", title
#print "------TITLE ENDS HERE------"

#print soup.title.string
#print soup.meta

# client = MongoClient()

# db = client["earth"]

# i=1
#hello = soup.find('table',{'class':'wikibase-entitytermsforlanguagelistview'})

#print hello

langlist = soup.findAll('li',{'class':'s-result-item'})

for products in range(1,len(langlist)):



	producthead=langlist[products].find('h2')
	
	v=producthead.get_text();

	print products
	print v


	#v= data.get('span class')                      #value is all href tags in a tag
	#db.coll.insert({str(i):v})               #writing in mongoDB using key,value 
#languages= langlist.findAll('li')

# for data in range(1,len(languages)):

# 	v= languages[data].get_text()
# 	db.coll.insert({str(i):v})

	
# 	print (languages[data].get_text())
# 	print "-------------------------------------------"
# 	i+=1

#db.coll.insert({"key":"val"})
#print(soup.get_text())
	