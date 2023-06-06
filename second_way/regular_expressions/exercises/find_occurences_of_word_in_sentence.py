import re

text = input()
search_word = input()

found_pattern = re.findall(rf"\b({search_word})\b", text, re.IGNORECASE)

print(len(found_pattern))