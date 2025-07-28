class Student:
    def __init__(self, name):
        self.name = name
        self.subjects = {}  # subject: marks

    def add_subject(self, subject, marks):
        self.subjects[subject] = marks

    def show_report(self):
        print(f"\nStudent Name: {self.name}")
        for subject, marks in self.subjects.items():
            print(f"{subject}: {marks} marks")


# Create student objects
student1 = Student("Divyang")
student2 = Student("Mann")
student3 = Student("Heli")

# Add subjects and marks
student1.add_subject("Math", 85)
student1.add_subject("Science", 92)
student1.add_subject("English", 92)

student2.add_subject("Math", 78)
student2.add_subject("English", 88)
student2.add_subject("Science", 88)

student3.add_subject("Math", 75)
student3.add_subject("English", 68)
student3.add_subject("Science", 98)

# Show reports
student1.show_report()
student2.show_report()
student3.show_report()
