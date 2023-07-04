class Ranking:
    __contests = {}
    __ranking_list = {}

    def __init__(self, contest, password, username=None, points=0):
        self.contest = contest
        self.password = password
        self.username = username
        self.points = int(points)
        self.logic()

    def add_contests(self):
        self.__contests[self.contest] = self.password

    def check_valid_contests(self):
        if self.contest in self.__contests and self.__contests[self.contest] == self.password:
            if self.username not in self.__ranking_list:
                self.__ranking_list[self.username] = {self.contest: self.points}
            elif self.contest not in self.__ranking_list[self.username]:
                self.__ranking_list[self.username][self.contest] = self.points
            elif self.__ranking_list[self.username][self.contest] < self.points:
                self.__ranking_list[self.username][self.contest] = self.points

    def logic(self):
        if not self.username:
            self.add_contests()
        else:
            self.check_valid_contests()

    @staticmethod
    def best_candidate():
        best_points = 0
        candidate = ""
        for name, points in Ranking.__ranking_list.items():
            if sum(points.values()) > best_points:
                best_points = sum(points.values())
                candidate = name

        return f"Best candidate is {candidate} with total {best_points} points."

    @staticmethod
    def sorted_ranking_list():

        for name, keys in sorted(Ranking.__ranking_list.items()):
            print(name)
            sorted_keys = dict(sorted(keys.items(), key=lambda x: x[1], reverse=True))
            for contest, points in sorted_keys.items():
                print(f"#  {contest} -> {points}")


while True:
    command = input()
    if ":" not in command:
        break
    contest, password = command.split(":")
    Ranking(contest, password)

while True:
    command = input()
    if "=>" not in command:
        print(Ranking.best_candidate())
        print("Ranking:")
        Ranking.sorted_ranking_list()

        break
    contest, password, username, points = command.split("=>")
    Ranking(contest, password, username, points)
