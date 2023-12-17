from mongoConnector import mongo_connector

class QuestionDao():
    def __init__(self):
        self.db = mongo_connector.db

    def get_random_question(self):
        question_collection = self.db["static"]
        qstn = next(question_collection.aggregate([{ "$sample": { "size": 1 } }]))
        if qstn:
            qstn["id"] = str(qstn["_id"])
            del qstn["_id"]
        return qstn


    def create_question(self,q):
        q_collection = self.db["static"]
        new_user = q_collection.insert_one(q)
        user = q_collection.find_one({"_id": new_user.inserted_id})
        user["id"] = str(user["_id"])
        user["_id"] = None
        return user

