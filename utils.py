from pymongo import MongoClient, ReturnDocument
from models.post import Post
import json
import settings

# database connection
#   MongoClient connection string required
#   dummy connection string :
#       "mongodb+srv://defaultUser:1234@cluster0.7z1zi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
#

# connect("mongodb+srv://defaultUser:1234@cluster0.7z1zi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

cluster = MongoClient(
    "mongodb+srv://user:user123@s-db.kktfx.mongodb.net/shurikendb?retryWrites=true&w=majority")

#   Database configurations are made here. These are the test DB values
#   Change values in need of use but dont change collection variable name
db = cluster["shurikendb"]
collection = db["posts"]


# inserting post to database in this method
# id automatically increments 1by1 and deleted id cannot be used again later
def insert_post(post):
    collection.insert_one({"_id": post.post_id, "json_body": json.dumps(post.json_value)})
    print(post)


# finding post by given id in this method
# return the found item so it can be used in other methods
def get_by_id(item_id):
    item_holder = collection.find_one({"_id": item_id})
    return item_holder


# delete method for DB
# finds the object by given id and deletes it from database
# print statements are there for debugging. Delete before going live
def delete_post(object_id):
    delete_query = {'_id': object_id}
    print("Deleting object number: ", object_id)
    db.delete_one(delete_query)
    print("Deleted object number: ", object_id)

# Updates post by given id and json_value
# not working yet
# def update_post(object_id, json_value):
#     print(db.find_one_and_update({"_id": object_id},
#                                          {"$set": {"json_value": json_value}},
#                                          return_document=ReturnDocument.AFTER))
