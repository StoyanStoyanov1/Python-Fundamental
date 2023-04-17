n = int(input())

for row in range(n + 1):
    print(" " * (n - row) + "*" * row + " | " + "*" * row + " " * (n - row))
