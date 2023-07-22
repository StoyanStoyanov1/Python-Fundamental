class NeedForSpeed:
    _MAX_TANK = 75

    def __init__(self, number_of_car):
        self.number_of_car = number_of_car
        self.cars = self.add_cars()
        self.logic()

    def add_cars(self):
        cars = {}
        for _ in range(self.number_of_car):
            car, mileage, fuel = input().split("|")
            cars[car] = {"Mileage": int(mileage), "Fuel": int(fuel)}

        return cars

    def drive(self, car, distance, fuel):
        if fuel <= self.cars[car]["Fuel"]:
            self.cars[car]["Fuel"] -= fuel
            self.cars[car]["Mileage"] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if self.cars[car]["Mileage"] >= 100000:
                print(f"Time to sell the {car}!")
                del self.cars[car]

        else:
            print("Not enough fuel to make that ride")

    def refuel(self, car, fuel):
        if self.cars[car]["Fuel"] + fuel > NeedForSpeed._MAX_TANK:
            print(f"{car} refueled with {NeedForSpeed._MAX_TANK - self.cars[car]['Fuel']} liters")
            self.cars[car]["Fuel"] = 75
        else:
            print(f"{car} refueled with {fuel} liters")
            self.cars[car]["Fuel"] += fuel

    def revert(self, car, kilometers):
        self.cars[car]["Mileage"] -= kilometers
        if self.cars[car]["Mileage"] < 10000:
            self.cars[car]["Mileage"] = 10000

        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")

    def logic(self):

        while True:
            command = input().split(" : ")
            if command[0] == "Stop":
                break

            if command[0] == "Drive":
                car, distance, fuel = command[1], int(command[2]), int(command[3])
                self.drive(car, distance, fuel)

            elif command[0] == "Refuel":
                car, fuel = command[1], int(command[2])
                self.refuel(car, fuel)

            elif command[0] == "Revert":
                car, kilometers = command[1], int(command[2])
                self.revert(car, kilometers)

    def result(self):
        return [f"{car} -> Mileage: {self.cars[car]['Mileage']} kms, Fuel in the tank: {self.cars[car]['Fuel']} lt." for
                car in self.cars.keys()]

    def __str__(self):
        return '\n'.join(self.result())


number_of_car = int(input())
print(NeedForSpeed(number_of_car))
