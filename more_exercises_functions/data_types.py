command = input()

result = None

if command == "int":
    number = int(input())
    result = number * 2

elif command == "real":
    number = float(input()) * 1.5
    result = f'{number:.2f}'


elif command == "string":
    text = input()
    result = "$" + text + "$"

print(result)