def rate(plants, plant, rating):

    if plant in plants:
        plants[plant]["Rating"].append(rating)

    else:
        print("error")


def update(plants, plant, new_rarity):
    if plant in plants:
        plants[plant]["Rarity"] = new_rarity

    else:
        print('error')


def reset(plants, plant):
    if plant in plants:
        plants[plant]["Rating"].clear()
    else:
        print('error')


def result(plants):
    print("Plants for the exhibition:")

    for plant in plants.keys():
        if len(plants[plant]['Rating']) > 0:
            plants[plant]["Rating"] = sum(plants[plant]['Rating']) / len(plants[plant]['Rating'])
        else:
            plants[plant]["Rating"] = 0
        print(f"- {plant}; Rarity: {plants[plant]['Rarity']}; Rating: {plants[plant]['Rating']:.2f}")


def plant_discovery_logic(count):
    plants = {}

    for _ in range(count):
        plant, rarity = input().split("<->")
        plants[plant] = {"Rarity": rarity, "Rating":[]}

    while True:
        command = input().split(": ")
        if command[0] == "Exhibition":
            result(plants)
            break

        elif command[0] == "Reset":
            reset(plants, command[1])

        elif command[0] == "Rate":
            plant, rating = command[1].split(" - ")
            rate(plants, plant, int(rating))

        elif command[0] == "Update":
            plant, new_rarity = command[1].split(" - ")
            update(plants, plant, new_rarity)


count = int(input())
plant_discovery_logic(count)