class PasswordReset:

    def __init__(self, current_password):
        self.current_password = current_password
        self.commands()

    def substitute(self, substring, substitute):
        if substring in self.current_password:
            self.current_password = self.current_password.replace(substring, substitute)
            print(self.current_password)
        else:
            print("Nothing to replace!")

    def cut(self, index, length):
        self.current_password = self.current_password[:length] + self.current_password[length + index:]
        print(self.current_password)

    def take_odd(self):
        self.current_password = self.current_password[1:len(self.current_password):2]
        print(self.current_password)

    def commands(self):
        while True:
            command = input()

            if command == "Done":
                break

            if command.startswith("TakeOdd"):
                self.take_odd()

            elif command.startswith("Cut"):
                _, length, index = command.split()
                self.cut(int(index), int(length))

            elif command.startswith("Substitute"):
                _, substring, substitute = command.split()
                self.substitute(substring, substitute)

    def __repr__(self):
        return f"Your password is: {self.current_password}"

password = input()
print(PasswordReset(password))