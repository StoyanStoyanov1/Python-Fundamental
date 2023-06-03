class EmoticonFinder:
    _emoticons = []

    def __init__(self, current_text):
        self.current_text = current_text
        self.find_emoticons()

    def find_emoticons(self):
        for index in range(len(self.current_text)):
            if self.current_text[index] == ":":
                self._emoticons.append(f":{self.current_text[index + 1]}")

    @staticmethod
    def all_emoticons():
        return "\n".join(EmoticonFinder._emoticons)


text = input()
EmoticonFinder(text)
print(EmoticonFinder.all_emoticons())
