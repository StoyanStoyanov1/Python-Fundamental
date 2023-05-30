class Capitals:

    def __init__(self, country, city):
        self.country = country.split(", ")
        self.city = city.split(", ")
        self.capitals = self.capitals()

    def capitals(self):
        capitals = {}
        for index in range(len(self.country)):
            capitals[self.country[index]] = self.city[index]

        return capitals

    def __repr__(self):
        return "\n".join([f"{key} -> {value}" for key, value in self.capitals.items()])


country, city = input(), input()
print(Capitals(country, city))
