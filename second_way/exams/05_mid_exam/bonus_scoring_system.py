class BonusScoringSystem:

    def __init__(self, number_of_students, number_of_lectures, additional_bonus):
        self.number_of_students = number_of_students
        self.number_of_lectures = number_of_lectures
        self.additional_bonus = additional_bonus
        self.max_bonus = self.find_max_bonus()

    def find_max_bonus(self):
        max_bonus = 0
        max_student_attendances = 0

        for student in range(self.number_of_students):
            student_attendances = int(input())

            current_bonus = student_attendances / self.number_of_lectures * (5 + self.additional_bonus)

            if current_bonus > max_bonus:
                max_bonus = current_bonus
                max_student_attendances = student_attendances

        return f"Max Bonus: {round(max_bonus)}.\nThe student has attended {max_student_attendances} lectures."

    def __repr__(self):
        return self.max_bonus


number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())
print(BonusScoringSystem(number_of_students, number_of_lectures, additional_bonus))
