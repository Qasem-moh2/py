import pymongo

myClient = pymongo.MongoClient("mongodb://localhost:27017/")

print(myClient.list_database_names())

mydb = myClient["test"]
myCloection = mydb["test"]
print(mydb.list_collection_names())
mydict = {"name": "John", "address": "Highway 37"}
x = myCloection.insert_one(mydict)

print(x)
for y in myCloection.find():
    print(y)
