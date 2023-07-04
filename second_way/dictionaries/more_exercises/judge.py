class Judge:
    __judge_register = {}

    def __init__(self, username, contest, points):
        self.username = username
        self.contest = contest
        self.points = int(points)
        self.registration()

    def registration(self):
        if self.contest not in self.__judge_register:
            self.__judge_register[self.contest] = {self.username: self.points}

        elif self.username not in self.__judge_register[self.contest]:
            self.__judge_register[self.contest][self.username] = self.points

        elif self.__judge_register[self.contest][self.username] < self.points:
            self.__judge_register[self.contest][self.username] = self.points

    @staticmethod
    def sorted_contests():
        names = {}
        for contest, current_names in Judge.__judge_register.items():
            print(f'{contest}: {len(current_names)} participants')
            sorted_names = dict(sorted(current_names.items(), key=lambda x: (-x[1], x[0])))
            counter = 0
            for name, points in sorted_names.items():
                counter += 1
                print(f"{counter}. {name} <::> {points}")
                if name not in names:
                    names[name] = points
                else:
                    names[name] += points

        return names

    @staticmethod
    def sorted_names():
        sorted_names = dict(sorted(Judge.sorted_contests().items(), key=lambda sort: (-sort[1], [sort[0]])))
        counter = 0
        print("Individual standings:")
        for name, points in sorted_names.items():
            counter += 1
            print(f"{counter}. {name} -> {points}")


while True:
    command = input()
    if "->" not in command:
        Judge.sorted_names()
        break
    name, contest, points = command.split(" -> ")
    Judge(name, contest, points)
