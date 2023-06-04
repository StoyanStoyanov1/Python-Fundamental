class ValidUsernames:
    _valid_usernames = []

    def __init__(self, usernames):
        self.usernames = usernames
        self.checking_username()

    def checking_username(self):
        for username in self.usernames:

            if len(username) in range(3, 17):
                is_valid = True
                for letter in username:
                    if not (letter.isalnum() or letter == "_" or letter == "-"):
                        is_valid = False

                if is_valid:
                    ValidUsernames._valid_usernames.append(username)
    @staticmethod
    def all_valid_usernames():
        return '\n'.join(ValidUsernames._valid_usernames)


usernames = input().split(", ")
ValidUsernames(usernames)
print(ValidUsernames.all_valid_usernames())
