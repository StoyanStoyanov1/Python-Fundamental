class TreasureHunt:

    def __init__(self, initial_loot, commands):
        self.initial_loot = initial_loot
        self.commands = commands
        self.logic = self.logic()

    def loot(self, items):
        for item in items:
            if item not in self.initial_loot:
                self.initial_loot.insert(0, item)

    def drop(self, index):
        if index in range(len(self.initial_loot)):
            current_loot = self.initial_loot.pop(index)
            self.initial_loot.append(current_loot)

    def steal(self, count):

        stolen_items = []
        for _ in range(count):
            if self.initial_loot:
                stole_item = self.initial_loot.pop(-1)
                stolen_items.append(stole_item)

        print(", ".join(stolen_items[::-1]))

    def logic(self):
        for command in self.commands:
            current_command, *items = command.split()
            if current_command == "Loot":
                self.loot(items)

            elif current_command == "Drop":
                self.drop(int(items[0]))

            elif current_command == "Steal":
                self.steal(int(items[0]))

    def __repr__(self):

        if self.initial_loot:
            average_gain = list(map(lambda x: len(x), self.initial_loot))

            return f"Average treasure gain: {sum(average_gain) / len(average_gain):.2f} pirate credits."

        return "Failed treasure hunt."


initial_loot = input().split("|")
commands = []

while True:
    command = input()
    if command == "Yohoho!":
        break

    commands.append(command)

print(TreasureHunt(initial_loot, commands))
