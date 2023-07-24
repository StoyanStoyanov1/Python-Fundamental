import re

text = input()
cool_threshold_sum = 1

for digit in re.findall("\d", text):
    cool_threshold_sum *= int(digit)

pattern = r"([:]{2}|[*]{2})([A-Z][a-z]{2,})\1"
found_emojis = re.findall(pattern, text)
cool_emojis = []


for emojis in found_emojis:
    if sum([ord(x) for x in emojis[1]]) >= cool_threshold_sum:
        cool_emojis.append(emojis[0] + emojis[1] + emojis[0])

print(f"Cool threshold: {cool_threshold_sum}\n{len(found_emojis)} emojis found in the text. The cool ones are:")
print('\n'.join(cool_emojis))

