class CharacterMultiplier:
    _sum_of_character = []

    def __init__(self, left_string, right_string):
        self.left_string = left_string
        self.right_string = right_string
        self.calculate_the_characters()

    def calculate_the_characters(self):
        index = 0
        while True:
            if index in range(len(self.left_string)) and index in range(len(self.right_string)):
                self._sum_of_character.append(ord(self.left_string[index]) * ord(self.right_string[index]))

            elif index in range(len(self.left_string)):
                self._sum_of_character.append(ord(self.left_string[index]))

            elif index in range(len(self.right_string)):
                self._sum_of_character.append(ord(self.right_string[index]))

            else:
                break

            index += 1

    @staticmethod
    def return_sum_of_character():
        return sum(CharacterMultiplier._sum_of_character)


left_string, right_string = input().split()
CharacterMultiplier(left_string, right_string)
print(CharacterMultiplier.return_sum_of_character())
