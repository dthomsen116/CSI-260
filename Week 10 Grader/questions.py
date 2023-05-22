class Question:
    _last_ID = 0

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def check(self, answer):
        return self.answer == answer
