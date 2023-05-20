time = list(map(int, input().split()))

left_car, right_car = 0, 0

for index in range(len(time) // 2):
    if time[index] != 0:
        left_car += time[index]
    else:
        left_car *= 0.8

for index in range(len(time) - 1, len(time) // 2, -1):
    if time[index] != 0:
        right_car += time[index]
    else:
        right_car *= 0.8

print(f"The winner is left with total time: {left_car:.1f}") if left_car < right_car else \
    print(f"The winner is right with total time: {right_car:.1f}")