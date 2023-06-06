import re

while True:
    text = input()
    if text:
        found_pattern = re.findall(r"\d+", text)
        if found_pattern:
            print(" ".join(found_pattern), end=" ")
    else:
        break
