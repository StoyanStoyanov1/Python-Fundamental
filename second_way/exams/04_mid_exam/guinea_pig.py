class GuineaPig:

    def __init__(self, food_grams, hay_grams, cover_grams, pig_weight):
        self.foot_grams = food_grams
        self.hay_grams = hay_grams
        self.cover_grams = cover_grams
        self.pig_weight = pig_weight
        self.days = 30
        self.enough_quantity = self.calculate()

    def calculate(self):
        counter_days = 0

        while counter_days < self.days:
            self.foot_grams -= 300

            counter_days += 1

            if counter_days % 2 == 0:
                self.hay_grams -= self.foot_grams * 0.05

            if counter_days % 3 == 0:
                self.cover_grams -= self.pig_weight / 3

            if self.foot_grams <= 0 or self.hay_grams <= 0 or self.cover_grams <= 0:
                return False

        return True

    def __repr__(self):
        if self.enough_quantity:
            return f"Everything is fine! Puppy is happy! Food: " \
                   f"{self.foot_grams / 1000:.2f}, Hay: {self.hay_grams / 1000:.2f}, " \
                   f"Cover: {self.cover_grams / 1000:.2f}."

        return "Merry must go to the pet store!"


food_grams = float(input()) * 1000
hay_grams = float(input()) * 1000
cover_grams = float(input()) * 1000
pig_weight = float(input()) * 1000

print(GuineaPig(food_grams, hay_grams, cover_grams, pig_weight))
