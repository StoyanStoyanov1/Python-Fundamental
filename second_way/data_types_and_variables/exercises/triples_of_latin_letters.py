n = int(input())

for first_letter in range(ord("a"), ord("a") + n):
    for second_letter in range(ord("a"), ord("a") + n):
        for three_letter in range(ord("a"), ord("a") + n) :
            print(chr(first_letter) + chr(second_letter) + chr(three_letter))
