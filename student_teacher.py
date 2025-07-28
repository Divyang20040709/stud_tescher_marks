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
student1 = Student("Aman")
student2 = Student("Divya")

# Add subjects and marks
student1.add_subject("Math", 85)
student1.add_subject("Science", 92)

student2.add_subject("Math", 78)
student2.add_subject("English", 88)

# Show reports
student1.show_report()
student2.show_report()