RANGE = {"Low": range(1, 51), "Medium": range(51, 81), "High": range(81, 126)}

fire = [item.split(" = ") for item in input().split("#")]
water = int(input())

effort = 0
total_fire = 0

print("Cells:")
for type_of_fire, value in fire:
    if int(value) in RANGE[type_of_fire]:
        if water - int(value) >= 0:
            water -= int(value)
            effort += int(value) * 0.25
            total_fire += int(value)
            print(f"- {value}")

print(f"Effort: {effort:.2f}\nTotal Fire: {total_fire}")
