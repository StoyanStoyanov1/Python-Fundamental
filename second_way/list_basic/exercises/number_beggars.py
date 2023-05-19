numbers = list(map(int, input().split(", ")))
count_of_beggars = int(input())

result = []
begin_index = 0

while count_of_beggars > len(result):
    sum_of_beggar = 0
    for index in range(begin_index, len(numbers), count_of_beggars):
        sum_of_beggar += numbers[index]
    result.append(sum_of_beggar)
    begin_index += 1

print(result)
