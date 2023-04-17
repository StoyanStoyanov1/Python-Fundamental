n = int(input())
left_right = (n - 1) // 2
stars = 1
if n % 2 == 0:
    stars += 1
for i in range(1, (n + 1) // 2):
    print("-" * left_right, end="")
    print("*", end="")

    mid = n - 2 * left_right - 2

    if mid >= 0:
        print("-" * mid, end="")
        print("*", end="")

    print("-" * left_right)
    left_right -= 1

for j in range(1, (n + 1) // 2):

    print("-" * left_right, end="")
    print("*", end="")

    mid = n - 2 * left_right - 2
    if mid >= 0:
        print("-" * mid, end="")
        print("*", end="")

    print("-" * left_right)
    left_right += 1
print("-" * left_right, end="")
print("*" * stars, end="")
print("-" * left_right)