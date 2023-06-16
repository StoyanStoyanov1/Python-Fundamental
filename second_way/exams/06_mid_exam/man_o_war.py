class ManOWar:

    def __init__(self, status_ship, status_warship, max_status):
        self.status_ship = status_ship
        self.status_warship = status_warship
        self.max_status = max_status
        self.commands()

    def fire(self, index, damage):
        if index in range(len(self.status_warship)):
            self.status_warship[index] -= damage
            if self.status_warship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                return True

    def defend(self, start_index, end_index, damage):
        if start_index in range(len(self.status_ship)) and end_index in range(len(self.status_ship)):
            for index in range(start_index, end_index + 1):
                self.status_ship[index] -= damage
                if self.status_ship[index] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    return True

    def repair(self, index, health):
        if index in range(len(self.status_ship)):
            self.status_ship[index] += health
            if self.status_ship[index] > self.max_status:
                self.status_ship[index] = self.max_status

    def status(self):
        count = 0

        for ship in self.status_ship:
            percent = ship / self.max_status * 100
            if percent < 20:
                count += 1

        return f"{count} sections need repair."

    def retire(self):
        return f"Pirate ship status: {sum(self.status_ship)}\nWarship status: {sum(self.status_warship)}"

    def commands(self):
        while True:
            command = input()
            if command == "Retire":
                print(self.retire())
                break

            if command == "Status":
                print(self.status())

            command = command.split()

            if command[0] == "Fire":
                index, damage = int(command[1]), int(command[2])
                fire = self.fire(index, damage)
                if fire:
                    break

            elif command[0] == "Defend":
                start_index, end_index, damage = int(command[1]), int(command[2]), int(command[3])
                defend = self.defend(start_index, end_index, damage)
                if defend:
                    break

            elif command[0] == "Repair":
                index, health = int(command[1]), int(command[2])
                self.repair(index, health)


status_ship = list(map(int, input().split(">")))
status_warship = list(map(int, input().split(">")))
max_status = int(input())
ManOWar(status_ship, status_warship, max_status)
