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

cluster = MongoClient("mongodb+srv://basar:Bb123@cluster0.tvsfk.mongodb.net/shuriken")

#   Database configurations are made here. These are the test DB values
#   Change values in need of use but dont change collection variable name
db = cluster["shuriken"]
collection = db["posts"]


# inserting post to database in this method
# id automatically increments 1by1 and deleted id cannot be used again later
def insert_post(json_value):
    post = Post(json_value=json_value)
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
def delete_post(object_id: int):
    delete_query = {'_id': object_id}
    collection.delete_one(delete_query)


# Updates post by given id and json_value

def update_post(object_id: int, json_value):
    collection.replace_one(
        {"_id": object_id},
        {
            "json_body": json_value
        }
    )