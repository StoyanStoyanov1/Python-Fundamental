class LettersChangeNumbers:
    def __init__(self, current_words):
        self.current_words = current_words
        self.result = 0

    def logic(self):
        for word in self.current_words:
            current_number = int(word[1:len(word) - 1])
            first_letter = word[0]
            second_letter = word[-1]
            lower_case = ord("a") - 1
            upper_case = ord("A") - 1
            if first_letter.isupper():
                first_letter_position = ord(first_letter) - upper_case
                self.result += current_number / first_letter_position

            elif first_letter.islower():
                first_letter_position = ord(first_letter) - lower_case
                self.result += current_number * first_letter_position

            if second_letter.isupper():
                second_letter_position = ord(second_letter) - upper_case
                self.result -= second_letter_position

            elif second_letter.islower():
                second_letter_position = ord(second_letter) - lower_case
                self.result += second_letter_position

        return f"{self.result:.2f}"


words = input().split()
letters_change_numbers = LettersChangeNumbers(words)
print(letters_change_numbers.logic())
