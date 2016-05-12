from pymongo import MongoClient
import re




y = raw_input("Data: ")

client = MongoClient()
db = client.jsondatabase
#db.jsoncollection.createIndex({"$**":"text"}, {weights: {"Content": 10, "Launch_Date": 5, "URL": 2}})
# cursor = db.jsoncollection.find({r'.*':y})

# cursor = db.jsoncollection.find({'Content': re.match( r'.*\y .*', line, re.M|re.I)})
cursor = db.jsoncollection.find({'$text':{'$search':y}})

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


