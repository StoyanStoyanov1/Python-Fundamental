class ComputerStore:
    __taxes = 0.20
    __special = 0.90
    _price_without_taxes = 0
    _total_taxes = 0

    def __init__(self, current_prices, current_command):
        self.current_prices = current_prices
        self.current_command = current_command
        self.calculate()

    def calculate(self):
        for price in self.current_prices:
            if price < 0:
                print("Invalid price!")
            else:
                self._price_without_taxes += price
                self._total_taxes += price * self.__taxes

    def total_price(self):
        total_price = self._price_without_taxes + self._total_taxes
        if self.current_command == "special":
            total_price *= self.__special
        return total_price

    def __repr__(self):
        if self._price_without_taxes:
            return f"Congratulations you've just bought a new computer!\n" \
                   f"Price without taxes: {self._price_without_taxes:.2f}$\n" \
                   f"Taxes: {self._total_taxes:.2f}$" \
                   f"\n-----------" \
                   f"\nTotal price: {self.total_price():.2f}$"

        else:
            return "Invalid order!"


prices = []

while True:
    command = input()
    if command == "special" or command == "regular":
        print(ComputerStore(prices, command))
        break
    prices.append(float(command))
