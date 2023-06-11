class CounterStrike:

    def __init__(self, current_energy):
        self.current_energy = current_energy

    def distance(self):
        distance = input()

        won_battles = 0

        while distance.isdigit():
            current_distance = int(distance)

            if current_distance in range(self.current_energy + 1):
                won_battles += 1
                self.current_energy -= current_distance
                if won_battles % 3 == 0:
                    self.current_energy += won_battles

            else:
                return f"Not enough energy! Game ends with {won_battles} won battles and {self.current_energy} energy"

            distance = input()

        return f"Won battles: {won_battles}. Energy left: {self.current_energy}"

    def __repr__(self):
        return self.distance()


energy = int(input())
print(CounterStrike(energy))
