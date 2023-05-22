import abc
import uuid


class Grader:
    def __init__(self):
        self.student_graders = {}
        self.assignment_classes = {}

    def register(self, assignment_class):
        if not issubclass(assignment_class, Assignment):
            raise RuntimeError("Your class does not have the right methods")

        id = uuid.uuid4()
        self.assignment_classes[id] = assignment_class
        return id

    def start_assignment(self, student, id):
        self.student_graders[student] = AssignmentGrader(
            student, self.assignment_classes[id])
        self.get_lesson(student)

    def get_lesson(self, student):
        assignment = self.student_graders[student]
        assignment.lesson()

    def check_assignment(self, student):
        assignment = self.student_graders[student]
        return assignment.check()

    def assignment_summary(self, student):
        grader = self.student_graders[student]
        return f"""
        {student}'s attempts at {grader.assignment.__class__.__name__}:

        attempts: {grader.attempts}
        correct: {grader.correct_attempts}

        passed: {grader.correct_attempts > 0}
        """


class Assignment(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def lesson(self, student):
        pass

    @abc.abstractmethod
    def check(self):
        pass

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Assignment:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True

        return NotImplemented


class AssignmentGrader:
    def __init__(self, student, AssignmentClass):
        self.assignment = AssignmentClass()
        print(self.assignment)
        self.assignment.student = student
        self.attempts = 0
        self.correct_attempts = 0

    def check(self):
        self.attempts = self.assignment.__class__.correct + self.assignment.__class__.incorrect
        self.correct_attempts = self.assignment.__class__.correct

    def lesson(self):
        self.assignment.lesson()

    def __str__(self):
        print("i am a ", self.assignment)
        return ""
