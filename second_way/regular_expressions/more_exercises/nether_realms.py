import re

health_pattern = r"[^\d\+\-*\/\.]"
damage_pattern = r"([-|+]?[\d+.\d]+)|([-|+]?[\d+])"
operator_pattern = r"[\/\*]"

for text in sorted(re.split(r", *", input())):
    text = text.strip()
    ascii_health = re.findall(health_pattern, text)
    find_damage = re.findall(damage_pattern, text)

    damage = sum([float(find[0]) for find in find_damage])
    health = sum([ord(symbol) for symbol in ascii_health])
    operator = re.findall(operator_pattern, text)

    for symbol in operator:
        if symbol == "*":
            damage *= 2
        else:
            damage /= 2

    print(f"{text} - {health} health, {damage:.2f} damage")

