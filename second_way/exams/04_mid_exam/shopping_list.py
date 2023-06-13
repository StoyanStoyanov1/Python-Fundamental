class ShoppingList:

    def __init__(self, products, commands):
        self.products = products
        self.commands = commands
        self.logic()

    def logic(self):
        for command in self.commands:
            current_command, *current_products = command.split()

            if current_command == "Urgent":
                self.urgent(current_products[0])

            elif current_command == "Unnecessary":
                self.unnecessary(current_products[0])

            elif current_command == "Correct":
                self.correct(current_products[0], current_products[1])

            elif current_command == "Rearrange":
                self.rearrange(current_products[0])

    def urgent(self, current_product):
        if current_product not in self.products:
            self.products.insert(0, current_product)

    def unnecessary(self, current_product):
        if current_product in self.products:
            self.products.remove(current_product)

    def correct(self, old_item, new_item):
        if old_item in self.products:
            index_old_item = self.products.index(old_item)
            self.products[index_old_item] = new_item

    def rearrange(self, current_product):
        if current_product in self.products:
            self.products.remove(current_product)
            self.products.append(current_product)

    def __repr__(self):
        return ", ".join(self.products)


products = input().split("!")
commands = []

command = input()
while command != "Go Shopping!":
    commands.append(command)
    command = input()

print(ShoppingList(products, commands))