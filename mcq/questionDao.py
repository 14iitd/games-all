from mongoConnector import mongo_connector


class QuestionDao():
    def __init__(self):
        self.db = mongo_connector.db

    def get_random_question(self,game="mcq"):
        question_collection = self.db["question"]
        qstn = next(question_collection.aggregate([ {"$match": {"game": game}},{"$sample": {"size": 1}}]))
        if qstn:
            qstn["id"] = str(qstn["_id"])
            del qstn["_id"]
        return qstn

    def submit_response(self, response):
        response_collection = self.db["response"]
        new_user = response_collection.insert_one(response.dict())
        user = response_collection.find_one({"_id": new_user.inserted_id})
        user["id"] = str(user["_id"])
        user["_id"] = None
        return user

    def create_question(self, q):
        q_collection = self.db["question"]
        new_user = q_collection.insert_one(q)
        user = q_collection.find_one({"_id": new_user.inserted_id})
        user["id"] = str(user["_id"])
        user["_id"] = None
        return user
