import re

text = input()
pattern = r"\b_([A-Za-z-0-9]+)\b"
found_pattern= re.findall(pattern, text)

print(",".join(found_pattern))