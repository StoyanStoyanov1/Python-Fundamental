WATER_CAPACITY = 255
n = int(input())
water = 0

for _ in range(n):
    liters_of_water = int(input())

    if liters_of_water + water > WATER_CAPACITY:
        print("Insufficient capacity!")
    else:
        water += liters_of_water

print(water)