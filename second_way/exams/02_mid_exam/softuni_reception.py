class SoftUniReception:

    def __init__(self, first_students_per_hour, second_students_per_hour, three_student_pers_hour, students_count):
        self.first_students_per_hour = first_students_per_hour
        self.second_students_per_hour = second_students_per_hour
        self.three_students_per_hour = three_student_pers_hour
        self.students_count = students_count

    def answer_the_questions(self):
        time_needed = 0

        while self.students_count > 0:
            time_needed += 1
            self.students_count -= \
                (self.first_students_per_hour + self.second_students_per_hour + self.three_students_per_hour)

            if time_needed % 4 == 0:
                time_needed += 1

        return time_needed

    def __repr__(self):
        return f"Time needed: {self.answer_the_questions()}h."


first_students_per_hour = int(input())
second_students_per_hour = int(input())
three_students_per_hour = int(input())
students_count = int(input())

print(SoftUniReception(first_students_per_hour, second_students_per_hour, three_students_per_hour, students_count))