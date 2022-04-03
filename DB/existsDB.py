import pymongo

myClient = pymongo.MongoClient("mongodb://localhost:27017/")

myDB = myClient["test"]
mycol=myDB['qasem']
dblist = myClient.list_database_names()

if "Qasdem" in dblist:
    print("The database exists.")
else:
    print("The database does not exist.")

print(myDB.list_collection_names())
print(dblist)