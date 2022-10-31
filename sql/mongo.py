import pymongo

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Replace <connection string> with your MongoDB deployment's connection string.
conn_str = "mongodb+srv://fomalhautn:u1O0KHjpZ1lXeYqU@cluster0.8t9kcae.mongodb.net/test"

# Set the Stable API version on the client.
client = pymongo.MongoClient(conn_str, server_api=ServerApi('1'), serverSelectionTimeoutMS=5000)
mydb = client["mydb"]
# print(mydb.list_collection_names())

mycol = mydb["customers"]
#print(mydb.list_collection_names())

#mydict = { "name": "John", "address": "Highway 37" }
#mycol.insert_one(mydict)

#mydb1 = client["customerDB"]
#print(mydb1.list_collection_names())

# insert info into the collection
'''
mydict = { "name": "AA", "address": "Stockholm" }
x = mycol.insert_one(mydict)
print(x.inserted_id)

mycol.insert_one({
    "name": "Linda",
    "orderdate": "6/10/2021",
    "species": "Dog",
    "Address": "380 W. Fir Ave",
})



mycol.find()
# update info in the collection

myquery = { "name": "Linda" }

mycol.update_one({"name": "Marsh"}, {"$set":{"Address": "451 W. Coffee St. A204"}})

'''

# delete info in the collection
myquery = { "name": "Linda" }
mycol.delete_one(myquery)