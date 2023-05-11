def themselves(n):
    cars = {}
    for _ in range(n):
        command = input().split("|")
        car, mileage, fuel = command[0], int(command[1]), int(command[2])
        cars[car] = {"Mileage": mileage, "Fuel": fuel}

    return cars


cars_themselves = themselves(int(input()))


def drive(cars, car, distance, fuel):
    if cars[car]['Fuel'] >= fuel:
        cars[car]['Fuel'] -= fuel
        cars[car]['Mileage'] += distance

        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
    else:
        print("Not enough fuel to make that ride")

    if cars[car]['Mileage'] > 100000:
        del cars[car]
        print(f"Time to sell the {car}!")


def refuel(cars, car, fuel):
    if cars[car]["Fuel"] + fuel <= 75:
        cars[car]["Fuel"] += fuel

    else:
        fuel = 75 - cars[car]['Fuel']
        cars[car]["Fuel"] = 75

    print(f"{car} refueled with {fuel} liters")


def revert(cars, car, kilometers):
    cars[car]["Mileage"] -= kilometers
    print(f"{car} mileage decreased by {kilometers} kilometers")


def stop(cars):
    for car in cars:
        print(f"{car} -> Mileage: {cars[car]['Mileage']} kms, Fuel in the tank: {cars[car]['Fuel']} lt.")



def need_for_speed_logic(cars):
    while True:
        command = input().split(" : ")
        if command[0] == "Stop":
            stop(cars)
            break

        if command[0] == "Drive":
            car, distance, fuel = command[1], int(command[2]), int(command[3])
            drive(cars, car, distance, fuel)

        elif command[0] == "Refuel":
            car, fuel = command[1], int(command[2])
            refuel(cars, car, fuel)

        elif command[0] == "Revert":
            car, kilometers = command[1], int(command[2])
            revert(cars, car, kilometers)


need_for_speed_logic(cars_themselves)
