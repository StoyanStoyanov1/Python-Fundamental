class HeroesOfCodeAndLogic:

    def __init__(self, number_of_heroes):
        self.number_of_heroes = number_of_heroes
        self.heroes = self.add_heroes()
        self.commands()
        self.still_alive = self.still_alive

    def add_heroes(self):
        heroes = {}
        for _ in range(self.number_of_heroes):
            hero_name, hp, mp = input().split()
            heroes[hero_name] = {"HP": int(hp), "MP": int(mp)}

        return heroes

    def cast_spell(self, hero_name, mp_needed, spell_name):
        if self.heroes[hero_name]["MP"] - mp_needed < 0:
            return f"{hero_name} does not have enough MP to cast {spell_name}!"

        self.heroes[hero_name]["MP"] -= mp_needed
        return f"{hero_name} has successfully cast {spell_name} and now has {self.heroes[hero_name]['MP']} MP!"

    def take_damage(self, hero_name, damage, attacker):
        self.heroes[hero_name]["HP"] -= damage
        if self.heroes[hero_name]["HP"] > 0:
            return f"{hero_name} was hit for {damage} HP by {attacker} and now has {self.heroes[hero_name]['HP']} HP left!"

        del self.heroes[hero_name]
        return f"{hero_name} has been killed by {attacker}!"

    def recharge(self, hero_name, amount):
        MAX_MP = 200
        self.heroes[hero_name]['MP'] += amount
        if self.heroes[hero_name]['MP'] > MAX_MP:
            recovered = amount - (self.heroes[hero_name]['MP'] - MAX_MP)
            self.heroes[hero_name]['MP'] = MAX_MP
            return f"{hero_name} recharged for {recovered} MP!"

        return f"{hero_name} recharged for {amount} MP!"

    def heal(self, hero_name, amount):
        MAX_HP = 100
        self.heroes[hero_name]['HP'] += amount
        if self.heroes[hero_name]['HP'] > MAX_HP:
            recovered = amount - (self.heroes[hero_name]['HP'] - MAX_HP)
            self.heroes[hero_name]['HP'] = MAX_HP
            return f"{hero_name} healed for {recovered} HP!"

        return f"{hero_name} healed for {amount} HP!"

    def commands(self):
        while True:
            command = input()
            if command == "End":
                break

            if command.startswith("CastSpell"):
                _, hero_name, mp_needed, spell_name = command.split(" - ")
                print(self.cast_spell(hero_name, int(mp_needed), spell_name))

            elif command.startswith("TakeDamage"):
                _, hero_name, damage, attacker = command.split(" - ")
                print(self.take_damage(hero_name, int(damage), attacker))

            elif command.startswith("Recharge"):
                _, hero_name, amount = command.split(" - ")
                print(self.recharge(hero_name, int(amount)))

            elif command.startswith("Heal"):
                _, hero_name, amount = command.split(" - ")
                print(self.heal(hero_name, int(amount)))

    def still_alive(self):
        result = []
        for hero, value in self.heroes.items():
            result.append(f"{hero}\n HP: {self.heroes[hero]['HP']}\n MP: {self.heroes[hero]['MP']}")

        return result

    def __repr__(self):
        return '\n'.join(self.still_alive())


number_of_heroes = int(input())
print(HeroesOfCodeAndLogic(number_of_heroes))
