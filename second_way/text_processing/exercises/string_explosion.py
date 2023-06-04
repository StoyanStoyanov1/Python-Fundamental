class StringExplosion:
    def __init__(self, current_text):
        self.current_text = current_text
        self.new_text = ""

    def logic(self):
        exploded = 0
        for index, symbol in enumerate(self.current_text):
            if self.current_text[index - 1] == ">":
                exploded += int(symbol)
                exploded -= 1

            elif symbol == ">":
                self.new_text += symbol

            elif exploded != 0:
                exploded -= 1

            else:
                self.new_text += symbol

        return self.new_text


text = input()
string_explosion = StringExplosion(text)
print(string_explosion.logic())
