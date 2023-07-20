import re
from math import floor


class AdAstra:
    foods = []

    def __init__(self, current_input):
        self.current_input = current_input
        self.need_kcal_a_day = 2000
        self.days = self.current_foods()

    def current_foods(self):
        pattern = r"(#|\|)([A-Za-z\s]+)\1((\d{2}/\/){3})\1(\d+)\1"
        found_food = re.findall(pattern, self.current_input)
        total_calorie = 0

        for food in found_food:
            name, date, calorie = food[1], food[2], int(food[3])
            self.foods.append(f"Item: {name}, Best before: {date}, Nutrition: {calorie}")
            total_calorie += calorie

        print(f"You have food to last you for: {floor(total_calorie / self.need_kcal_a_day)} days!")

    def __repr__(self):
        return '\n'.join(self.foods)


print(AdAstra(input()))