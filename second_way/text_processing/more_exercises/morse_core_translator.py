class MorseCodeTranslator:
    def __init__(self, current_morse_code):
        self.current_morse_code = current_morse_code

    def translate(self):
        translated_text = ""

        morse_code_dict = \
            {
                ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E",
                "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J",
                "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O",
                ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
                "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y",
                "--..": "Z"
            }

        for morse_code in self.current_morse_code:
            for code in morse_code.split():
                translated_text += morse_code_dict[code]
            translated_text += " "

        return translated_text


morse_code = input().split(" | ")
print(MorseCodeTranslator(morse_code).translate())
