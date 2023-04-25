import re

text = input()

pattern = r"(=|/)([A-Z][A-Za-z]{2,})\1"
result_pattern = re.findall(pattern, text)

destinations = [dest[1] for dest in result_pattern]
travel_points = [len(dest) for dest in destinations]

print(f"Destinations: {', '.join(destinations)}\nTravel Points: {sum(travel_points)}")