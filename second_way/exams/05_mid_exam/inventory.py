class Inventory:

    def __init__(self, current_items, commands):
        self.current_items = current_items
        self.commands = commands
        self.logic()
    def renew(self, item):
        if item in self.current_items:
            self.current_items.append(self.current_items.pop(self.current_items.index(item)))

    def collect(self, item):
        if item not in self.current_items:
            self.current_items.append(item)

    def drop(self, item):
        if item in self.current_items:
            self.current_items.remove(item)

    def combine_items(self, old_item, new_item):
        if old_item in self.current_items:
            self.current_items.insert(self.current_items.index(old_item) + 1, new_item)

    def logic(self):
        for command in self.commands:
            if command[0] == "Collect":
                self.collect(command[1])

            elif command[0] == "Drop":
                self.drop(command[1])

            elif command[0] == "Combine Items":
                old_item, new_item = command[1].split(":")
                self.combine_items(old_item, new_item)

            elif command[0] == "Renew":
                self.renew(command[1])

    def __repr__(self):
        return ", ".join(self.current_items)


items = input().split(", ")

commands = []

while True:
    command = input()
    if command == "Craft!":
        break

    commands.append(command.split(" - "))


print(Inventory(items, commands))
