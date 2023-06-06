import re

text = input()
pattern = r"\s(([a-z]+[a-z\-\.\_]+)@([a-z\-]+)(\.[a-z]+)+)\b"
found_pattern = re.findall(pattern, text)

for found in found_pattern:
    print(found[0])