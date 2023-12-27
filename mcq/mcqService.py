from mcq.questionDao import QuestionDao
import random

class McqService():
    def __init__(self):
        self.dao = QuestionDao()

    def get_random_question(self):
        q= self.dao.get_random_question(game="mcq")
        color_list = ["FAFAFB", "FFFFFF", "D3C1FA", "FFF3F0", "B9E5FF", "FFF0AF", "FFC9E2"]
        q["color"] = random.choice(color_list)
        q["accuracy"] = 10
        q["played"] = 1221
        return q

    def create_question(self, question):
        return self.dao.create_question(question)
    def sumbit_response(self,user_response):
        self.dao.submit_response(user_response)
