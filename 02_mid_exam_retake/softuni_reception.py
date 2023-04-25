first_employees, second_employees, three_employees = int(input()), int(input()), int(input())

number_of_students = int(input())
hours = 0

while number_of_students > 0:
    hours += 1
    if hours % 4 == 0:
        continue
    number_of_students -= (first_employees + second_employees + three_employees)

print(f"Time needed: {hours}h.")