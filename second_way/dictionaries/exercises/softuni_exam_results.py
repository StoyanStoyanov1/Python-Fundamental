class SoftUniExamResults:
    __exam_results = {}
    __counter = {}

    def __init__(self, username, language, points=None):
        self.username = username
        self.language = language
        self.points = points
        self.logic()

    def add_usernames(self):
        if self.language not in self.__exam_results:
            self.__exam_results[self.language] = {self.username: self.points}
            self.__counter[self.language] = 1

        elif self.username not in self.__exam_results[language]:
            self.__exam_results[self.language][self.username] = self.points
            self.__counter[self.language] += 1

        else:
            if self.__exam_results[self.language][self.username] < self.points:
                self.__exam_results[self.language][self.username] = self.points
            self.__counter[self.language] += 1

    def banned_username(self):
        for language, usernames in self.__exam_results.items():
            for name in usernames:
                if name == self.username:
                    del self.__exam_results[language][name]
                    break

    def logic(self):
        if self.language == "banned":
            self.banned_username()
        else:
            self.add_usernames()

    @staticmethod
    def exam_results():
        result = []

        result.append("Results:")

        for usernames in SoftUniExamResults.__exam_results.values():
            for name, points in usernames.items():
                result.append(name + " | " + str(points))

        result.append("Submissions:")

        for language, count in SoftUniExamResults.__counter.items():
            result.append(language + " - " + str(count))

        return "\n".join(result)


while True:
    command = input()
    if "-" not in command:
        print(SoftUniExamResults.exam_results())
        break

    if command.count("-") == 1:
        username, language = command.split("-")
        SoftUniExamResults(username, language)
    else:
        username, language, points = command.split("-")
        SoftUniExamResults(username, language, int(points))
