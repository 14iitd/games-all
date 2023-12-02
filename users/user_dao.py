from mongoConnector import mongo_connector
from utils import convert_to_str


class UserDao():
    def __init__(self):
        self.db = mongo_connector.db

    def get_user_by_device(self, email):
        user_collection = self.db["users"]
        user = user_collection.find_one({"email": email})
        if user:
            user["id"] = str(user["_id"])
            user["_id"] = None
        return user

    def create_user(self, user_data):
        user_collection = self.db["users"]
        new_user = user_collection.insert_one(user_data)
        user = user_collection.find_one({"_id": new_user.inserted_id})
        user["id"] = str(user["_id"])
        user["_id"] = None
        return user



