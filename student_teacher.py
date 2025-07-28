class User:
    def __init__(self, name):
        self.name = name


class Teacher(User):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"Teacher: {self.name}"


class Student(User):
    def __init__(self, name):
        super().__init__(name)
        self.subjects = {}  # Dictionary: { subject: marks }

    def add_subject(self, subject, marks):
        self.subjects[subject] = marks

    def get_marks(self, subject):
        return self.subjects.get(subject, "No such subject found")

    def print_report(self):
        print(f"\nReport Card for {self.name}")
        for subject, marks in self.subjects.items():
            print(f"{subject}: {marks} marks")

    def __str__(self):
        return f"Student: {self.name}"


# 👨‍🏫 Create a Teacher
teacher1 = Teacher("Mr. X")

# 👨‍🎓 Create Students
student1 = Student("Divyang")
student2 = Student("Mann")
student3 = Student("Heli")

# 📚 Add Subjects and Marks
student1.add_subject("Math", 85)
student1.add_subject("English", 80)
student1.add_subject("Science", 92)

student2.add_subject("Math", 78)
student2.add_subject("English", 78)
student2.add_subject("Science", 88)

student3.add_subject("Math", 89)
student3.add_subject("English", 78)
student3.add_subject("Science", 85)

# 🖨️ Print Reports
print(teacher1)

print(student1)
student1.print_report()

print(student2)
student2.print_report()

print(student3)
student3.print_report()
