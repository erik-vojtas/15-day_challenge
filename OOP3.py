
# Define the classes (Student, Exam, University) so that following
# Excerpt of code from a Student Management System works as expected.
import random

class Student:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
        self.exams = {}

    def takeExam(self, exam):
        grade = random.randint(1,5)
        self.exams[exam.name] = grade
        exam.examTaken(self)

class University:
    def __init__(self, name):
        self.name = name
        self.list_of_students = []

    def enroll(self, student):
        self.list_of_students.append(student)

    def stats(self):
        for s in self.list_of_students:
            print(f"{s.name} took {len(s.exams)} exam(s).")
            for k, v in s.exams.items():
                print(f"\tGot {v} in {k}.")


class Exam:
    def __init__(self, name):
        self.name = name
        self.students = []

    def examTaken(self, student):
        self.students.append(student)

    def calculateAvgGrade(self):
        sum = 0
        for s in self.students:
            if self.name in s.exams:
                sum += s.exams[self.name]
        return sum/len(self.students)

    def stats(self):
        print(f"{self.name} exam was taken by {len(self.students)} students. Average score = {self.calculateAvgGrade()}")


s1= Student ("Sandy", "24.01.1992") # name, dob
s2= Student ("Spili", "14.10.1993") # name, dob
s3= Student ("Waile", "04.06.1994") # name, dob

imc = University ("FH Krems")

imc.enroll(s1)
imc.enroll(s2)
imc.enroll(s3)
e1 = Exam("Programming II")
e2 = Exam("Software Eng")
e3 = Exam("Creativity")
# assign a random value as grade s1.takeExam (e1)
s2.takeExam(e1)
s2.takeExam(e3)
s3.takeExam(e1)
s1.takeExam(e2)
s2.takeExam(e2)
s1.takeExam(e3)
s3.takeExam(e3)
# print statistics
imc.stats()

#exams statistics
e1.stats()
e2.stats()
e3.stats()


