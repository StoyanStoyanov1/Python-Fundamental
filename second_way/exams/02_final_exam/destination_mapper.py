import re


class DestinationMapper:

    def __init__(self, current_text):
        self.current_text = current_text
        self.destinations = self.find_travel_points()

    def find_travel_points(self):
        pattern = r"(=|\/)([A-Z][A-Za-z]{2,})\1"
        matches = re.findall(pattern, self.current_text)

        return [x[1] for x in matches]

    def __repr__(self):
        return f"Destinations: {', '.join(self.destinations)}\nTravel Points: {sum([len(x) for x in self.destinations])}"

text = input()
print(DestinationMapper(text))
