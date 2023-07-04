class DragonArmy:
    _dragons = {}

    def __init__(self, color, name, damage, health, armor):
        self.color = color
        self.name = name
        self.damage = 45 if damage == "null" else int(damage)
        self.health = 250 if health == "null" else int(health)
        self.armor = 10 if armor == "null" else int(armor)
        self.add_dragons()

    def add_dragons(self):
        if self.color not in self._dragons:
            self._dragons[self.color] = {self.name: {"damage": self.damage, "health": self.health, "armor": self.armor}}
        else:
            self._dragons[self.color][self.name] = {"damage": self.damage, "health": self.health, "armor": self.armor}

    @staticmethod
    def result():
        for color, dragon in DragonArmy._dragons.items():
            damage = [damage["damage"] for damage in dragon.values()]
            health = [health["health"] for health in dragon.values()]
            armor = [armor["armor"] for armor in dragon.values()]
            average_damage = sum(damage) / len(damage)
            average_health = sum(health) / len(health)
            average_armor = sum(armor) / len(armor)
            print(f"{color}::({average_damage:.2f}/{average_health:.2f}/{average_armor:.2f})")
            for dragon_name, values in sorted(dragon.items()):
                print(f"-{dragon_name} -> damage: {values['damage']}, "
                      f"health: {values['health']}, armor: {values['armor']}")


for _ in range(int(input())):
    color, name, damage, health, armor = input().split()
    DragonArmy(color, name, damage, health, armor)

DragonArmy.result()
