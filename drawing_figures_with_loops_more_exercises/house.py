n = int(input())

stars = 1
even = n % 2 == 0
dash = (n - stars) // 2

if even:
    range_row = n // 2
    stars += 1
else:
    range_row = n // 2 + 1

for _ in range(range_row):
    print("-" * dash + "*" * stars + "-" * dash)
    stars += 2
    dash = (n - stars) // 2

rows = n - range_row

for _ in range(rows):
    print("|" + "*" * (n - 2) + "|")