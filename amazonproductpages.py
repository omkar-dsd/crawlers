from bs4 import BeautifulSoup as bs
from pymongo import MongoClient
import urllib2

# PROXY HANDLER----

proxy=urllib2.ProxyHandler({})
opener=urllib2.build_opener(proxy)
opener.addheaders=[('User-agent','Mozilla/5.0')]
urllib2.install_opener(opener)

# PROXY HANDLER END -----------


# LINK EXTRACTOR FUNCTION-----

# def linkExtractor(urltoopen, tag1, attrib1, attrib1value, tag2 ,attrib2, attrib2value, finalAttrib):
# 	url = urllib2.urlopen(urltoopen).read()
# 	soup = bs(url)

# 	result = soup.findAll(tag1,{attrib1:attrib1value})
# 	hreflist = []

	
# 	for i in range(0,len(result)):
# 		resultDetails = result[i].find(tag2,{attrib2:attrib2value})
# 		link = resultDetails[finalAttrib]
# 		hreflist.append(link)      # appends links into array
		
# 	return hreflist     # returns list of fetched links

# #FUNCTION END----------


#

def allPages(soup):

	lastpagetag = soup.find('span', {'class' : 'pagnDisabled'})
	
	lastpagenumber = lastpagetag.get_text()

	pageslist = []

	

	for i in range(1,int(lastpagenumber)):


		nextpagetag = soup.find('span', {'class':'pagnRA'})
		nextpagehref = nextpagetag.a['href']
		nextpagelink = "http://www.amazon.com" + nextpagehref 

		pageslist.append(nextpagelink)

		url = urllib2.urlopen(nextpagelink).read()
		soup = bs(url)

		print i-1
		print pageslist[i-1]


	return pageslist


def forPrinter(x):
	for i in range(1,len(x)):
		print i
		print x[i]

nextpagelink = "http://www.amazon.com/s/ref=nb_sb_noss_2/185-5945162-0333204?url=search-alias%3Daps&field-keywords=laptop"
url = urllib2.urlopen(nextpagelink).read()
soup = bs(url)
pageslink = allPages(soup)

#forPrinter(pageslink)


