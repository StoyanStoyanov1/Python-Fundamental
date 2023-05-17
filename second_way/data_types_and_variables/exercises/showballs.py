n = int(input())

highest_snowball_value = 0
result = ""

for _ in range(n):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = int((snowball_weight / snowball_time) ** snowball_quality)
    if snowball_value > highest_snowball_value:
        highest_snowball_value = snowball_value
        result = f"{snowball_weight} : {snowball_time} = {snowball_value} ({snowball_quality})"

print(result)