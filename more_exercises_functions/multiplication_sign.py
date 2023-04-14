numbers = [int(input()) for num in range(3)]

if 0 in numbers:
    print("zero")

else:
    counter = 0
    for num in numbers:
        if num < 0:
            counter += 1
    print("negative") if counter % 2 != 0 else print('positive')
