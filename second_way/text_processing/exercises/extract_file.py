text = input().split("\\")

result = text[-1].split(".")

print(f"File name: {result[0]}\nFile extension: {result[1]}")