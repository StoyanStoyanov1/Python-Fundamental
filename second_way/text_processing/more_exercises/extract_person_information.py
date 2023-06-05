class ExtractPersonInformation:

    def __init__(self, current_text):
        self.current_text = current_text

    def find_the_person(self):
        symbols_index = [self.current_text.index("@"), self.current_text.index("|"),
                         self.current_text.index("#"), self.current_text.index("*")]

        name, age = self.current_text[symbols_index[0] + 1:symbols_index[1]], \
            self.current_text[symbols_index[2] + 1:symbols_index[3]]

        return f"{name} is {age} years old."


for _ in range(int(input())):
    text = input()
    extract_person = ExtractPersonInformation(text)
    print(extract_person.find_the_person())
