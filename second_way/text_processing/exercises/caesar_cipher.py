class CaesarCipher:
    _encrypted_version = ""

    def __init__(self, current_text):
        self.current_text = current_text
        self.make_a_encrypted_version()

    def make_a_encrypted_version(self):
        for symbol in self.current_text:
            self._encrypted_version += chr(ord(symbol) + 3)

        print(self._encrypted_version)


text = input()
CaesarCipher(text)
