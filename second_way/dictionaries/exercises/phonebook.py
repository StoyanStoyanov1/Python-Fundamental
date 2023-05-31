class Phonebook:
    __phonebook = {}

    def add_phonenumbers(self):
        phone = input()
        while not phone.isdigit():
            name, phone_number = phone.split("-")
            self.__phonebook[name] = phone_number
            phone = input()

        return int(phone)

    def exist_phone(self):
        exist_phone = []
        for _ in range(self.add_phonenumbers()):
            name = input()
            if name in self.__phonebook:
                exist_phone.append(f"{name} -> {self.__phonebook[name]}")
            else:
                exist_phone.append(f"Contact {name} does not exist.")
        return exist_phone

    def __repr__(self):
        return '\n'.join(self.exist_phone())


print(Phonebook())
