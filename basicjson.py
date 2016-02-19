import urllib2
import simplejson

url="http://www.amazon.com/s/ref=nb_sb_noss_2/185-5945162-0333204?url=search-alias%3Daps&field-keywords=laptop"

if __name__ == "__main__":
	req = urllib2.Request(url)
	opener = urllib2.open(req)
	json = simplejson.load(f)

	for item in json:
		print item.get('id')

