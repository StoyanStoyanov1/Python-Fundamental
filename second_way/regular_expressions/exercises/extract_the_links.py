import re

current_info = input()
pattern = r"(www.([A-Za-z0-9\-]+)(\.[a-z]+)+)"

while current_info:
    found_pattern = re.search(pattern, current_info)
    if found_pattern:
        print(found_pattern.group())
    current_info = input()