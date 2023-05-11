import re

text = input()

pattern = r"(@|#)([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1"

result_pattern = re.findall(pattern, text)

if result_pattern:
    print(f"{len(result_pattern)} word pairs found!")
else:
    print("No word pairs found!")

find_mirror = []

for find in result_pattern:
    first_word = find[1]
    second_word = find[2]
    if first_word == second_word[::-1]:
        find_mirror.append(f"{first_word} <=> {second_word}")

if find_mirror:
    print("The mirror words are:")
    print(", ".join(find_mirror))
else:
    print("No mirror words!")