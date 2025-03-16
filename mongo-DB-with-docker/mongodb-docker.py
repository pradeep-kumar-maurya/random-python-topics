from pymongo import MongoClient

mongo_username = 'admin'
mongo_password = 'admin'
mongo_db_name = 'mongodb'
mongo_db_host = 'localhost'
mongo_port = 27017
mongo_uri = f'mongodb://{mongo_username}:{mongo_password}@{mongo_db_host}:{mongo_port}'

# connect to MongoDB
client = MongoClient(mongo_uri)

# create (or access) a database
db = client['my_database']

# create (or access) a collection
collection = db['my_collection']

# insert one document in collection
collection.insert_one(
    {"name": "Pradeep", "age": 26, "city": "Hyderabad"}
)

# insert multiple documents in collection
collection.insert_many([
    {"name": "Alice", "age": 30, "city": "NYC"},
    {"name": "Bob", "age": 35, "city": "LA"},
])

# get databases
databases = client.list_database_names()
print("DBs in MongoDB ->", databases)

# find one document
one_doc = collection.find_one({'name': 'Pradeep'})
print("individual document ->", one_doc)

# # find all documents
all_docs = collection.find({})
print("All documents")
for doc in all_docs:
    print(doc)


client.close()
