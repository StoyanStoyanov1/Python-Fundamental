class HeartDelivery:

    def __init__(self, houses, jumps):
        self.houses = houses
        self.jumps = jumps
        self.result = self.logic()

    def logic(self):

        current_index = 0
        valentines_days = 0

        for jump in self.jumps:

            current_index += jump
            if current_index >= len(self.houses):
                current_index = 0

            if self.houses[current_index] == 0:
                print(f"Place {current_index} already had Valentine's day.")

            else:
                self.houses[current_index] -= 2

                if self.houses[current_index] == 0:
                    valentines_days += 1
                    print(f"Place {current_index} has Valentine's day.")

        return current_index, valentines_days

    def __repr__(self):
        failed_places = len(self.houses) - self.result[1]

        if failed_places:
            return f"Cupid's last position was {self.result[0]}.\nCupid has failed {failed_places} places."

        else:
            return f"Cupid's last position was {self.result[0]}.\nMission was successful."


houses = list(map(int, input().split("@")))

jumps = []

jump = input()

while jump != "Love!":
    jumps.append(int(jump.split()[1]))
    jump = input()

print(HeartDelivery(houses, jumps))
