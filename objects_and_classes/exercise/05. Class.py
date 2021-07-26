class Class:
    __students_count = 22

    def __init__(self, name):
        self.name, self.students, self.grades = name, [], []

    def add_student(self, name: str, grade: float):
        if len(self.students) < Class.__students_count:
            self.students.append(name), self.grades.append(grade)

    def get_average_grade(self):
        return sum(self.grades) / len(self.grades)

    def __repr__(self):
        return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {self.get_average_grade():.2f}"
