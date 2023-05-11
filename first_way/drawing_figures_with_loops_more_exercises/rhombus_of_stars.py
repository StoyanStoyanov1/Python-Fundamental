n = int(input())

for row in range(1, n + 1):
    print(' ' * (n - row) + "* " * row)

for rows in range(1, n + 1):
    print(' ' * rows + "* " * (n - rows))