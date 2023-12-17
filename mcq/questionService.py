from mcq.questionDao import QuestionDao


class QuestionService():
    def __init__(self):
        self.dao = QuestionDao()

    def get_random_question(self):
        return self.dao.get_random_question()

    def create_question(self, question):
        return self.dao.create_question(question)
