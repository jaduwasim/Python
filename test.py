from pymongo import MongoClient
con = MongoClient('localhost',port=27017)
db = con['Practice_DB']
coll = db['Employee_Coll']
documents = coll.find({'$and':[{'esal':{'$gt':2000}},{'esal':{'$lt':5000}}]})
for doc in documents:
	print(doc)
	print('-'*80)