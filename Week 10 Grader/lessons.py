from grader import Assignment
from questions import Question


#class IntroToPython(Assignment):
class IntroToPython(Assignment):
    questions = []
    correct = 0
    incorrect = 0

    def __init__(self):
        IntroToPython.questions.append(
            Question(
                "What symbol is used to print the remainder while dividing?",
                "%"))

        IntroToPython.questions.append(
            Question("Store the value '$20' to the variable 'price'.",
                     "price=$20"))

        IntroToPython.questions.append(
            Question("Print 'Test' to the console", "print('test')"))

    def lesson(self):
        for i in range(len(IntroToPython.questions)):
            cor_ans = False

        while not cor_ans:
            print(IntroToPython.questions[i].question)
            userans = input()

            if self.check(i, userans):
                IntroToPython.correct += 1
                cor_ans = True
            else:
                IntroToPython.incorrect += 1
                print("XXXXXX_WRONG ANSWER_XXXXXXX")

    def check(self, pos, ans):
        return IntroToPython.questions[pos].check(ans)
