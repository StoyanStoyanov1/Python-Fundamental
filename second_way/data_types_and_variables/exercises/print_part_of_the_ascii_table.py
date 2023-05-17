start_char = int(input())
end_char = int(input())

result = [chr(symbol) for symbol in range(start_char, end_char + 1)]
print(" ".join(result))