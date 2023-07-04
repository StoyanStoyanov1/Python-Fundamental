class MobaChallenger:
    __players = {}
    __best_players = {}

    def __init__(self, player, position, skill=-1):
        self.player = player
        self.position = position
        self.skill = int(skill)
        self.logic()

    def add_players(self):
        if self.player not in self.__players:
            self.__players[self.player] = {self.position: self.skill}

        elif self.position not in self.__players[self.player]:
            self.__players[self.player][self.position] = self.skill

        elif self.__players[self.player][self.position] < self.skill:
            self.__players[self.player][self.position] = self.skill

    def duel(self, first_player, second_player):
        if (first_player and second_player) in self.__players:
            for position in self.__players[first_player]:
                if position in self.__players[second_player]:
                    first_player_total_skills = sum(self.__players[first_player].values())
                    second_player_total_skills = sum(self.__players[second_player].values())
                    if first_player_total_skills < second_player_total_skills:
                        del self.__players[first_player]
                    elif second_player_total_skills < first_player_total_skills:
                        del self.__players[second_player]
                    break

    def logic(self):
        if self.skill != -1:
            self.add_players()
        else:
            self.duel(self.player, self.position)



    @staticmethod
    def sorted_result():
        for player, position in MobaChallenger.__players.items():
            MobaChallenger.__best_players[player] = sum(position.values())

        players = dict(sorted(MobaChallenger.__best_players.items(), key=lambda player: (-player[1], player[0])))

        for player, skills in players.items():
            print(f"{player}: {skills} skill")
            positions = dict(sorted(MobaChallenger.__players[player].items(), key=lambda sort: (-sort[1], sort[0])))
            for position, skill in positions.items():
                print(f"- {position} <::> {skill}")


while True:
    command = input()
    if "->" in command:
        player, position, skill = command.split(" -> ")
        MobaChallenger(player, position, skill)

    elif " vs " in command:
        first_player, second_player = command.split(" vs ")
        MobaChallenger(first_player, second_player)

    else:
        MobaChallenger.sorted_result()
        break
