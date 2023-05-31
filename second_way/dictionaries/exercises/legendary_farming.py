class LegendaryFarming:
    __legendary_items = {"shards": [250, "Shadowmourne"], "fragments": [250, "Valanyr"], "motes": [250, "Dragonwrath"]}
    received_items = {"shards": 0, "fragments": 0, "motes": 0}

    def current_stones(self):

        while True:
            current_stones = input().lower().split()

            for index in range(0, len(current_stones), 2):
                stone = current_stones[index + 1]
                value = int(current_stones[index])

                if stone not in self.received_items:
                    self.received_items[stone] = value
                else:
                    self.received_items[stone] += value

                if stone in self.__legendary_items:

                    if self.received_items[stone] >= self.__legendary_items[stone][0]:
                        self.received_items[stone] -= self.__legendary_items[stone][0]
                        return self.__legendary_items[stone][1]

    def __repr__(self):

        return f"{self.current_stones()} obtained!\n" + \
            "\n".join([f'{stone}: {value}' for stone, value in self.received_items.items()])


print(LegendaryFarming())
