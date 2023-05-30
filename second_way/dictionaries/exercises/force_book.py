class ForceBook:
    __force_book = {}

    def __init__(self, current_text):
        self.current_text = current_text
        self.add_force_users()

    def add_force_users(self):
        if "|" in self.current_text:
            force, user = self.current_text.split(" | ")
            if force not in self.__force_book:
                self.__force_book[force] = []

            user_is_valid = [True for value in self.__force_book.values() if user in value]
            if not user_is_valid:
                self.__force_book[force].append(user)

        elif "->" in self.current_text:
            user, force = self.current_text.split(" -> ")
            if force not in self.__force_book:
                self.__force_book[force] = []
            if user not in self.__force_book[force]:
                self.__force_book[force].append(user)
                print(f"{user} joins the {force} side!")

            for current_force, current_user in self.__force_book.items():
                if current_force == force:
                    continue
                if user in current_user and len(current_user) > 1:
                    self.__force_book[current_force].pop(current_user)
                elif user in current_user:
                    del self.__force_book[current_force]
                    break

    @staticmethod
    def return_users():
        result = []
        for side, users in ForceBook.__force_book.items():
            if len(users) == 0:
                continue
            result.append(f"Side: {side}, Members: {len(users)}")
            for user in users:
                result.append(f"! {user}")

        return "\n".join(result)


while True:
    text = input()
    if text == "Lumpawaroo":
        print(ForceBook.return_users())
        break

    ForceBook(text)
