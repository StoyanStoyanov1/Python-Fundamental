class CountCharsInAString:
    result = []

    def __init__(self, text):
        self.text = text
        self.characters = {}

    def counter_of_characters(self):
        for char in self.text:
            if char not in self.characters and char != " ":
                self.characters[char] = self.text.count(char)

    def add_result(self):
        CountCharsInAString.counter_of_characters(self)
        for key, value in self.characters.items():
            CountCharsInAString.result.append(f"{key} -> {value}")

    def __repr__(self):
        CountCharsInAString.add_result(self)
        return "\n".join(CountCharsInAString.result)


text = CountCharsInAString(input())

print(text)
