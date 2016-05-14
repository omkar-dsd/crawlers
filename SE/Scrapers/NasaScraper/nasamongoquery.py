from pymongo import MongoClient
import pymongo
import re




userquery = raw_input("")
#mongodb://192.168.101.5:27017/'
client = MongoClient('mongodb://192.168.101.5:27017/')
db = client.nasadb
#db.nasacollection.create_index({"$**":"text"}, {"weights": {"Content": 10, "Launch_Date": 5, "URL": 2}})



#CREATE INDEX WHEN RUNNING CRAWLER FOR THE FIRST TIME------------------------

# db.nasacollection.ensure_index([
#       ('Content', 'text'),
#       ('Launch_Date', 'text'),
#       ('Phase','text')
#   ],
#   name="nasadb_index",
#   weights={
#       'Phase':2,
#       'Content':10,
#       'Launch_Date':5	
#   }
# )
# CREATE INDEX END ----------------------------------



#db.nasacollection.create_index("Content")

#cursor = db.nasacollection.find({r'.*':userquery})
# cursor = db.jsoncollection.find({'Content': re.match( r'.*\y .*', line, re.M|re.I)})

cursor = db.nasacollection.find({'$text':{'$search': userquery}})

# cursor = db.jsoncollection.find()

for document in cursor:
	

	# MISSION NAME SECTION
	missionName = str(document['Content'])
	missionName = missionName.replace("[u'","")
	missionName = missionName.replace("']","")
	missionName = missionName.replace("\\t","")
	missionName = missionName.replace("\\n","")

	print "Mission : ", missionName

	
	# MISSION LAUNCH DATE SECTION
	launchDate = str(document['Launch_Date'])
	launchDate = launchDate.replace("\\t","")
	#launchDate = re.sub('[\\\][tn]', '', launchDate)
	launchDate = launchDate.replace("[u'","")
	launchDate = launchDate.replace("\\n","")
	launchDate = launchDate.replace("']","")
	launchDate = launchDate.replace("  ","")
	
	print "Launch Date : ", launchDate
	#print "Launch Date : ", str(document['Launch_Date']).strip()

	#MISSION WORKING PHASE SECTION
	missionPhase = str(document['Phase'])
	missionPhase = missionPhase.replace("[u'","")
	missionPhase = missionPhase.replace("']","")
	missionPhase = missionPhase.replace("\\t","")
	missionPhase = missionPhase.replace("\\n","")

	print "Operating Phase : ", missionPhase
	#print "Operating Phase : ", document['Phase']
	print " "
	print " "