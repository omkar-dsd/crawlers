from pymongo import MongoClient
import re


y = raw_input("Data: ")

client = MongoClient()
db = client.jsondatabase

# cursor = db.jsoncollection.find({r'.*':y})

cursor = db.jsoncollection.find()

print cursor
textmatch = re.compile("COral Reef Airborne Laboratory")

for document in cursor:
	print re.match(textmatch, document)