class RageQuit:
    def __init__(self, current_text):
        self.current_text = current_text

    def rage_quit(self):
        unique_symbols = ""
        current_text = ""
        finish_text = ""
        number = ""
        flag = False
        for index, letter in enumerate(self.current_text):
            if flag:
                flag = False
                continue

            if not letter.isdigit() and letter not in unique_symbols:
                unique_symbols += letter

            if not letter.isdigit():
                current_text += letter
            else:
                number += letter
                if index + 1 in range(len(self.current_text)) and self.current_text[index + 1].isdigit():
                    number += self.current_text[index + 1]
                    flag = True
                finish_text += current_text * int(number)
                number = ""
                current_text = ""

        return f"Unique symbols used: {len(unique_symbols)}\n{finish_text}"


text = input().upper()
rage_quit = RageQuit(text)
print(rage_quit.rage_quit())
