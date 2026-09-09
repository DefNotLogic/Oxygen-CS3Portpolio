class Student:
    def __init__(self, name):
        self.name = name

class School:
    def __init__(self, name):
        self.name = name
        self.students = [] #listofstudents

    def add_student(self, student):
        self.students.append(student)

#Example Usage
school = School("Emarsi")
s1 = Student("Topilo")
s2 = Student("Marquez")
school.add_student(s1)
school.add_student(s2)

print(f"School Name: ", school.name)
print(f"List of Students: ")
for student in school.students:
    print(f"- {student.name}")
    




