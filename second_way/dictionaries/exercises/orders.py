class Orders:
    __orders = {}
    current_command_buy = False

    def __init__(self, order, price: float, count: int):
        self.current_order = order
        self.current_price = float(price)
        self.current_count = int(count)
        self.price_list()

    def price_list(self):
        if self.current_order not in self.__orders:
            self.__orders[self.current_order] = {"price": self.current_price, "count": self.current_count}
        else:
            self.__orders[self.current_order]["count"] += self.current_count
            self.__orders[self.current_order]["price"] = self.current_price

    @staticmethod
    def result():
        if Orders.current_command_buy:
            result = {}
            for order, value in Orders.__orders.items():
                result[order] = value["count"] * value["price"]

            return '\n'.join([f"{order} -> {price:.2f}" for order, price in result.items()])


while True:
    command = input()
    if command == "buy":
        Orders.current_command_buy = True
        print(Orders.result())
        break
    order, price, count = command.split()
    Orders(order, price, count)
