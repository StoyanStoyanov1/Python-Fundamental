key = int(input())
n = int(input())
letters = [input() for _ in range(n)]

result = map(lambda letter: chr(ord(letter) + key), letters)

print("".join(result))