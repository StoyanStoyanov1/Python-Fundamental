import re

text = input()
pattern = r'(#|@)([[a-z]{3,})\1{2}([[a-z]{3,})\1'
matches = re.findall(pattern, text, re.IGNORECASE)

if matches:
    print(f"{len(matches)} word pairs found!")
    mirrors = [f"{word[1]} <=> {word[2]}" for word in matches if word[1] == word[2][::-1]]
    print(f"The mirror words are:\n{', '.join(mirrors)}") if mirrors else print("No mirror words!")

else:
    print("No word pairs found!\nNo mirror words!")