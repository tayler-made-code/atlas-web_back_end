#!/usr/bin/env python3
""" provides some stats about Nginx logs stored in MongoDB """
import pymongo
from pymongo import MongoClient

""" connect to MongoDB """
client = MongoClient('mongodb://localhost:27017/')
db = client.logs
collection = db['nginx']

""" count the number of documents in the collection """
total_docs = collection.count_documents({})
print(f"{total_docs} logs")

""" count documents by method """
print("Methods:")
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
for method in methods:
    count = collection.count_documents({"method": method})
    print(f"\tmethod {method}: {count}")

""" count status checks """
status_check_count = collection.count_documents({"method": "GET", "path": "/status"})
print(f"{status_check_count} status check")
