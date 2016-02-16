from pymongo import MongoClient
from bs4 import BeautifulSoup
import urllib2

#----- PROXY HANDLER -------
proxy=urllib2.ProxyHandler({})
opener=urllib2.build_opener(proxy)
opener.addheaders=[('User-agent','Mozilla/5.0')]
urllib2.install_opener(opener)
#----- END PROXY HANDLER ------


#----- Function to extract links from page ----

def linkExtractor(urltoopen, tag1, attrb1, attrib1value, tag2, attrb2, attrib2value, finalattrib):

	urlhtmlreader = urllib2.urlopen(urltoopen).read()
	soup = BeautifulSoup(urlhtmlreader)


	result = soup.findAll(tag1,{attrb1:attrib1value})
	hreflist = []

	for i in range(0,len(result)):

		resultDetails = result[i].find(tag2,{attrb2:attrib2value})
		link = resultDetails(finalattrib)
		hreflist.append(link)              # adding links to arrays

	return hreflist   # returning the arraylist containing links

# ----- Function END


url = "http://www.amazon.com/s/ref=nb_sb_noss_2/185-5945162-0333204?url=search-alias%3Daps&field-keywords=laptop"
links = linkExtractor(url,"li","class","s-result-item","a","class","a-link-normal","href")
for i in range(0,len(links)):

	print i
	print links[i]