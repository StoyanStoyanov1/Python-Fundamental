class SoftUniParking:
    __register = []
    book_register = {}

    def __init__(self, command, name, number=None):
        self.command = command
        self.name = name
        self.number = number

    def register(self):
        if self.name not in self.book_register:
            self.book_register[self.name] = self.number
            return f"{self.name} registered {self.number} successfully"

        else:
            return f"ERROR: already registered with plate number {self.number}"

    def unregister(self):
        if self.name in self.book_register:
            del self.book_register[self.name]
            return f"{self.name} unregistered successfully"

        else:
            return f"ERROR: user {self.name} not found"

    def __repr__(self):
        if self.command == "register":
            return self.register()

        elif self.command == "unregister":
            return self.unregister()

    @staticmethod
    def registers():
        return "\n".join(f"{name} => {number}" for name, number in SoftUniParking.book_register.items())


for _ in range(int(input())):
    the_command = input().split()

    if len(the_command) > 2:
        command, name, number = the_command
        print(SoftUniParking(command, name, number))
    else:
        command, name = the_command
        print(SoftUniParking(command, name))

print(SoftUniParking.registers())
