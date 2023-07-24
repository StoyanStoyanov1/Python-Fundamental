class ActivationKeys:

    def __init__(self, current_key):
        self.current_key = current_key
        self.commands()

    def contains(self, substring):
        if substring in self.current_key:
            return f"{self.current_key} contains {substring}"
        else:
            return "Substring not found!"

    def flip(self, upper_or_lower, start_index, end_index):
        if upper_or_lower == "Upper":
            self.current_key = self.current_key[:start_index] + \
                               self.current_key[start_index:end_index].upper() + self.current_key[end_index:]
        else:
            self.current_key = self.current_key[:start_index] + \
                               self.current_key[start_index:end_index].lower() + self.current_key[end_index:]

        return self.current_key

    def slice(self, start_index, end_index):
        self.current_key = self.current_key[:start_index] + self.current_key[end_index:]
        return self.current_key

    def commands(self):
        while True:
            command, *data = input().split(">>>")

            if command == "Generate":
                break

            if command == "Contains":
                substring = data[0]
                print(self.contains(substring))

            elif command == "Flip":
                upper_or_lower, start_index, end_index = data[0], int(data[1]), int(data[2])
                print(self.flip(upper_or_lower, start_index, end_index))


            elif command == "Slice":
                start_index, end_index = int(data[0]), int(data[1])
                print(self.slice(start_index, end_index))

    def __repr__(self):
        return f"Your activation key is: {self.current_key}"


key = input()
print(ActivationKeys(key))
