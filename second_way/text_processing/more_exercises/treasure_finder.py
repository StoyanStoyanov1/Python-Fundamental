class Treasure_finder:
    def __init__(self, keys, current_text):
        self.keys = keys
        self.current_text = current_text

    def find_treasure(self):
        new_text = ""
        key = 0
        for index in range(len(self.current_text)):
            if key not in range(0, len(self.keys)):
                key = 0

            new_text += chr(ord(self.current_text[index]) - self.keys[key])

            key += 1

        type_coordinates = new_text[new_text.index("&") + 1:new_text.index("&", new_text.index("&") + 1)]
        found_coordinates = new_text[new_text.index("<") + 1: new_text.index(">")]

        return f"Found {type_coordinates} at {found_coordinates}"


keys = list(map(int, input().split()))
while True:
    text = input()
    if text == "find":
        break

    print(Treasure_finder(keys, text).find_treasure())
