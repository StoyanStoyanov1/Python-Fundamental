class ReplaceChars:
    def __init__(self, current_text):
        self.current_text = current_text
        self._new_text = ""
        self.replace_chars()

    def replace_chars(self):
        for index, letter in enumerate(self.current_text):
            if index < len(self.current_text) - 1 and letter == self.current_text[index + 1]:
                continue
            self._new_text += letter

    def return_new_text(self):
        return self._new_text


text = input()
replace_chars_instance = ReplaceChars(text)
print(replace_chars_instance.return_new_text())