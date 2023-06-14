class MuOnline:
    health = 100
    bitcoins = 0
    dead = False

    def __init__(self, current_room, current_number):
        self.current_rum = current_room
        self.current_number = int(current_number)
        self.logic()

    def potion(self):

        print(f"You healed for {100 - MuOnline.health} hp.") if MuOnline.health + self.current_number > 100 \
            else print(f"You healed for {self.current_number} hp.")

        MuOnline.health = 100 if MuOnline.health + self.current_number > 100 else MuOnline.health + self.current_number

        print(f"Current health: {MuOnline.health} hp.")

    def chest(self):
        MuOnline.bitcoins += self.current_number

        print(f"You found {self.current_number} bitcoins.")

    def other_rum(self):
        MuOnline.health -= self.current_number
        if MuOnline.health > 0:
            print(f"You slayed {self.current_rum}.")
        else:
            MuOnline.dead = True
            print(f"You died! Killed by {self.current_rum}.")

    def logic(self):
        if self.current_rum == "potion":
            self.potion()

        elif self.current_rum == "chest":
            self.chest()

        else:
            self.other_rum()


for number_of_room, room in enumerate(input().split("|")):
    current_room, current_number = room.split()
    MuOnline(current_room, current_number)
    if MuOnline.dead:
        print(f"Best room: {number_of_room + 1}")
        break

if not MuOnline.dead:
    print("You've made it!")
    print(f"Bitcoins: {MuOnline.bitcoins}")
    print(f"Health: {MuOnline.health}")
