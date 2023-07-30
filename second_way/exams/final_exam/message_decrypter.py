import re

n = int(input())

word_pattern = r"^(\$|%)([A-Z][a-z]{2,})\1"
number_pattern = r"(\[(\d+)])\|"
for _ in range(n):
    text = input()
    found_text = re.findall(word_pattern, text)
    found_number = re.findall(number_pattern, text)
    if found_text and len(found_number) == 3:
        current_text = found_text[0][1]

        message = ''.join(chr(int(num[1])) for num in found_number)
        print(current_text + ": " + message)

    else:
        print("Valid message not found!")
