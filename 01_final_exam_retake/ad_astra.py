from math import floor
import re
text = input()
pattern = r"(#|\|)([A-Za-z\s]+)\1(\d{2}/\d{2}/\d{2})\1(\d+)\1"
matches = re.findall(pattern, text)

NEEDED_CALORIE_FOR_A_DAY = 2000

product, date, calorie = [], [], []

for match in matches:
    product.append(match[1])
    date.append(match[2])
    calorie.append(int(match[3]))

print(f"You have food to last you for: {floor(sum(calorie) / NEEDED_CALORIE_FOR_A_DAY)} days!")

for index in range(len(product)):
    print(f"Item: {product[index]}, Best before: {date[index]}, Nutrition: {calorie[index]}")
    