class Pirates:

    def __init__(self):
        self.cities = self.add_cities()
        self.commands()

    def add_cities(self):
        cities = {}

        while True:
            command = input()
            if command == "Sail":
                break

            city, population, gold = command.split("||")
            if city not in cities:
                cities[city] = {"Population": 0, "Gold": 0}
            cities[city]["Population"] += int(population)
            cities[city]["Gold"] += int(gold)

        return cities

    def plunder(self, town, people, gold):
        self.cities[town]["Population"] -= people
        self.cities[town]["Gold"] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

        if self.cities[town]["Population"] <= 0 or self.cities[town]["Gold"] <= 0:
            print(f"{town} has been wiped off the map!")
            del self.cities[town]

    def prosper(self, town, gold):
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            self.cities[town]["Gold"] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {self.cities[town]['Gold']} gold.")

    def commands(self):
        while True:
            command = input()
            if command.startswith("End"):
                break

            if command.startswith("Plunder"):
                _, town, people, gold = command.split("=>")
                self.plunder(town, int(people), int(gold))

            elif command.startswith("Prosper"):
                _, town, gold = command.split("=>")
                self.prosper(town, int(gold))

    def result(self):
        result = []
        if self.cities:
            result.append(f"Ahoy, Captain! There are {len(self.cities.keys())} wealthy settlements to go to:")
            for town in self.cities.keys():
                result.append(f"{town} -> Population: "
                              f"{self.cities[town]['Population']} citizens, Gold: {self.cities[town]['Gold']} kg")

        return result

    def __repr__(self):
        if self.result():
            return '\n'.join(self.result())

        return "Ahoy, Captain! All targets have been plundered and destroyed!"


print(Pirates())
