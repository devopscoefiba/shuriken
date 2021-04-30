from pymongo import MongoClient

# database connection
#   MongoClient connection string required
#   dummy connection string :
#       "mongodb+srv://defaultUser:1234@cluster0.7z1zi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
#
cluster = MongoClient(
    "mongodb+srv://defaultUser:1234@cluster0.7z1zi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = cluster["shurikendb"]
collection = db["shuriken"]
