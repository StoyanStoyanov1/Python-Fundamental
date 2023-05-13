n = int(input())
characters = [",", ".", "_"]

for _ in range(n):
    output = "is pure."
    text = input()

    for symbol in text:
        if symbol in characters:
            output = "is not pure!"
            break

    print(f"{text} {output}")

