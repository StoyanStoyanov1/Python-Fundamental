import re

pattern = r"@([A-Z][a-z]+)[^@\-!:>]*:\d+[^@\-!:>]*!(A|D)![^@\-!:>]*->\d+"
attacked_planet = []
destroyed_planet = []

for _ in range(int(input())):
    current_text = input()
    key = len(re.findall(r"[star]", current_text.lower()))
    new_text = ""

    for letter in current_text:
        new_text += chr(ord(letter) - key)

    found_info = re.search(pattern, new_text)
    if found_info:
        attack_type, planet = found_info.group(2), found_info.group(1)
        if attack_type == "A":
            attacked_planet.append(planet)
        elif attack_type == "D":
            destroyed_planet.append(planet)

print(f"Attacked planets: {len(attacked_planet)}")

for planet in sorted(attacked_planet):
    print("->", planet)

print(f"Destroyed planets: {len(destroyed_planet)}")

for planet in sorted(destroyed_planet):
    print("->", planet)




