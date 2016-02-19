from pymongo import MongoClient #importing Mongo Library
from bs4 import BeautifulSoup   #importing bs library
import urllib2

#----- PROXY HANDLER -------
proxy=urllib2.ProxyHandler({})
opener=urllib2.build_opener(proxy)
opener.addheaders=[('User-agent','Mozilla/5.0')]
urllib2.install_opener(opener)
#----- END PROXY HANDLER ------

url = "http://www.amazon.com/s/ref=nb_sb_noss_2/185-5945162-0333204?url=search-alias%3Daps&field-keywords=laptop"

urlopener = urllib2.urlopen(url)
urlHtml = urlopener.read()      #Extracts Complete Html or Page Source from read url.

urlHtml_soup = BeautifulSoup(urlHtml)  #Storing Html in Soup, to process with beautiful soup

soup_ul = urlHtml_soup.find('ul', {'id':'s-results-list-atf'})

soup_ul_li = soup_ul.findAll('li')

#storing in mongo

client = MongoClient()
db = client['amazon']

#print len(soup_ul_li)

for data in range(1,len(soup_ul_li)):

	#print data

	result_id = soup_ul_li[data].get('id')
	data_asin = soup_ul_li[data].get('data-asin')
	

	db.col.insert({str(result_id): str(data_asin)})

print "Entry Successful!"


#mongo
#use amazon
# db.col.find().toArray().

#db.col.drop()

