class BlackFlag:

    def __init__(self, days, plunder_for_a_day, expected_plunder):
        self.days = days
        self.plunder_for_a_day = plunder_for_a_day
        self.expected_plunder = expected_plunder
        self.total_plunder = 0
        self.calculate()

    def calculate(self):
        for day in range(1, self.days + 1):
            self.total_plunder += self.plunder_for_a_day
            if day % 3 == 0:
                self.total_plunder += self.plunder_for_a_day * 0.5

            if day % 5 == 0:
                self.total_plunder *= 0.70

    def __repr__(self):
        if self.total_plunder >= self.expected_plunder:
            return f"Ahoy! {self.total_plunder:.2f} plunder gained."
        else:
            return f"Collected only {self.total_plunder / self.expected_plunder * 100:.2f}% of the plunder."


days = int(input())
plunder_for_a_day = int(input())
expected_plunder = int(input())
print(BlackFlag(days, plunder_for_a_day, expected_plunder))
