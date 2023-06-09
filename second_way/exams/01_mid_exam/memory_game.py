class MemoryGame:

    def __init__(self, elements, indexes):
        self.elements = elements
        self.indexes = indexes
        self.result = self.logic()

    def remove_element(self, found_element):
        self.elements.remove(found_element), self.elements.remove(found_element)

    def insert_element(self, turns):
        self.elements.insert(len(self.elements) // 2, f"-{turns}a")
        self.elements.insert(len(self.elements) // 2, f"-{turns}a")

    def print_result(self, current_result):
        print(current_result)

    def logic(self):
        won = False
        turns = 0

        for indexes in self.indexes:

            current_indexes = indexes.split()
            first_index, second_index = int(current_indexes[0]), int(current_indexes[1])
            turns += 1

            if first_index not in range(len(self.elements)) \
                    or second_index not in range(len(self.elements)) \
                    or first_index == second_index:
                self.print_result("Invalid input! Adding additional elements to the board")
                self.insert_element(turns)
                continue

            if self.elements[first_index] == self.elements[second_index]:

                found_element = elements[first_index]
                self.remove_element(found_element)
                self.print_result(f"Congrats! You have found matching elements - {found_element}!")

            else:
                self.print_result("Try again!")

            if not self.elements:
                won = True
                self.print_result(f"You have won in {turns} turns!")
                break

        if not won:
            self.print_result(f"Sorry you lose :(\n{' '.join(elements)}")


elements = input().split()
indexes = []
while True:
    current_indexes = input()
    if current_indexes == "end":
        break
    indexes.append(current_indexes)

MemoryGame(elements, indexes)
