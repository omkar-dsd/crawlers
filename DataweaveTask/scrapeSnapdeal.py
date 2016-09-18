#---SOURCE CODE BY : OMKAR ------------

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import urllib2
import json


def proxyHandler():

	#----- PROXY HANDLER -------
	proxy=urllib2.ProxyHandler({})
	opener=urllib2.build_opener(proxy)
	opener.addheaders=[('User-agent','Mozilla/5.0')]
	urllib2.install_opener(opener)
	#----- END PROXY HANDLER ------

def extractProductInfo(productURL, productTitle):
	#This function extracts the specification from each product page

	proxyHandler()

	bsoupFile = urllib2.urlopen(productURL)
	bsoupHtml = bsoupFile.read()					#Html of Page
	inner_soup = BeautifulSoup(bsoupHtml, "lxml") 		#BeautifulSoup Object

	sections = {}									#Dictionary to store each product's each section - JSON FORMAT
	title_sections = {}								#Parent Dictionary  - JSON FORMAT

	specList = inner_soup.findAll('table',{'class':'product-spec'})  #getting all tables

	#LOOP to get data from tables
	for i in range(len(specList)):

		#Finds the section heads
		table_head = specList[i].find('th')

		#Finds the Product Deatails contained within that section
		table_data = specList[i].findAll('td')
		
		heads =[]              							#Stores the product description keys       
		values = []			   							#Stores the product description values	
		odd_or_even = 0		   							#key - value - key - value pattern in list

		#LOOP to store table data into list
		for k in table_data:
			if odd_or_even%2 == 0:
				heads.append(k.getText())        		#storing keys
			else:
				values.append(k.getText())		 		#Storing values

			odd_or_even = odd_or_even + 1		 		#Incrementing


		section_spec = {}						

		#LOOP to make entries in dictionary
		for i in range(len(heads)):
			section_spec.update({heads[i]:values[i]})


		sections.update({table_head.getText():section_spec})		#Updating dictionary
		

	title_sections.update({productTitle:sections})					#Updating Parent Dictionary
	ten_product_list.append(title_sections)							#Appending into Global list



driver = webdriver.Firefox()										#Starts browser
driver.implicitly_wait(20)											
driver.get("https://www.snapdeal.com/products/mobiles-mobile-phones?sort=plrty")	

elem = driver.find_element_by_id("see-more-products")
ActionChains(driver).move_to_element(elem).perform()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

soup = BeautifulSoup(driver.page_source, "lxml")					#Soup object
driver.close()


productSection = soup.findAll('section',{'data-dpcol':'c'})			#Each section has 4 products
tuple_desc = soup.findAll('div',{'class':'product-tuple-description'})

count = 0					#Counter
product_dict_list = []		#Stores JSON of product detail
product_pages = []			#Stores href of each product
product_title = []

#Loop to get data of sections
for products in range(len(productSection)):


	productSource = productSection[products].findAll('source')

 	for c in productSource:
		count = count + 1

		a_tags = tuple_desc[count-1].find('a')['href']
		price = tuple_desc[count-1].find('span')

		product_dict = {'ID': count, "PRODUCT" : c['title'], 'PRICE' : price.getText(), 'Thumbnail' : c['srcset'], 'PRDT-PAGE' : a_tags }
		product_pages.append(a_tags)
		product_title.append(c['title'])
		product_dict_list.append(product_dict)


mainPageJSON = open('mainPage.json', 'w')							#creating a file mainPage.json in same folder as this file
mainPageJSON.write(json.dumps(product_dict_list, indent = 4))   	#Storing outerpage products in json form.

ten_product_list = []

#LOOP to get each Product Page from function created above.
for j in range(0,10):
	extractProductInfo(product_pages[j],product_title[j])   	#Calls the above created function to extract information

innerPageJSON = open('innerPage.json', 'w')							#creating a file in same folder as this file
innerPageJSON.write(json.dumps(ten_product_list, indent = 4))		#Storing Each product page info in JSON



#-------------END OF CODE-----------
#-------------SOURCE CODE BY : OMKAR-----------------
