import re

pattern = r"%([A-Z][a-z]+)%[^\.\$\%\|]*?<(\w+)>[^\.\%\$\|]*?\|(\d+)\|[^\.\%\$\|]*?(\d+\.?\d*)\$"

total_income = 0
while True:
    current_text = input()
    if current_text == "end of shift":
        print(f"Total income: {total_income:.2f}")
        break

    found_info = re.search(pattern, current_text)

    if found_info:
        name, item, = found_info.group(1), found_info.group(2)
        income = int(found_info.group(3)) * float(found_info.group(4))
        total_income += income
        print(f"{name}: {item} - {income:.2f}")
