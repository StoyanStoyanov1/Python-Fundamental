counter = int(input())

the_sum = [1]
result = [1]

for count in range(counter - 1):
    if len(the_sum) >= 4:
        remove = the_sum.pop(0)
    result.append(sum(the_sum))
    the_sum.append(sum(the_sum))

result = [str(result) for result in result]
print(" ".join(result))
