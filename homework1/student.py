class Student:

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = []


class CFGStudent(Student):

    def add_subject(self, subject):
        self.subjects.append(subject)

    def view_subjects(self):
        subs = []
        for i in range(len(self.subjects)):
            subs.append(self.subjects[i]['title'])
        print(f"Student {self.name} has taken following subjects: \n")
        print(subs)
        print("\n")

    def view_marks(self):
        total_marks = 0
        for i in range(len(self.subjects)):
            total_marks += self.subjects[i]['marks']

        average_marks = total_marks / len(self.subjects)

        print(f"Average Marks for {self.name}: {average_marks}")


shiwani = CFGStudent('shiwani', 29, 10)
shiwani.add_subject({'title': 'python', 'marks': 90})
shiwani.add_subject({'title': 'mysql', 'marks': 95})

shiwani.view_subjects()
shiwani.view_marks()