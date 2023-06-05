class ASCIISimulator:

    def __init__(self, begin_ascii_symbol, end_ascii_symbol, current_text):
        self.begin_ascii_symbol = begin_ascii_symbol
        self.end_ascii_symbol = end_ascii_symbol
        self.current_text = current_text

    def sum_of_found_characters(self):
        sum_of_found_characters = 0
        for symbol in self.current_text:
            if ord(self.begin_ascii_symbol) < ord(symbol) < ord(self.end_ascii_symbol):
                sum_of_found_characters += ord(symbol)

        return sum_of_found_characters


begin_ascii_symbol = input()
end_ascii_symbol = input()
text = input()
ascii_simulator = ASCIISimulator(begin_ascii_symbol, end_ascii_symbol, text)
print(ascii_simulator.sum_of_found_characters())
