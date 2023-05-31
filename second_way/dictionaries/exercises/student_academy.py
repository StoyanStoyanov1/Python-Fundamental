class StudentAcademy:
    __students_grades = {}

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.add_grades()

    def add_grades(self):
        if self.name not in self.__students_grades:
            self.__students_grades[self.name] = []
        self.__students_grades[self.name].append(self.grade)

    @staticmethod
    def nice_students():
        result = []
        for name, grades in StudentAcademy.__students_grades.items():
            average_grade = round(sum(grades) / len(grades), 2)
            if average_grade >= 4.50:
                result.append(f"{name} -> {average_grade:.2f}")

        return "\n".join(result)

for _ in range(int(input())):
    name, grade = input(), float(input())
    StudentAcademy(name, grade)

print(StudentAcademy.nice_students())