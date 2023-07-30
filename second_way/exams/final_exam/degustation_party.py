def like(party, guest, meal):
    if guest not in party:
        party[guest] = []

    if meal not in party[guest]:
        party[guest].append(meal)

    return party


def dislike(party, guest, meal, counter):

    if guest not in party:
        print(f"{guest} is not at the party.")

    elif meal not in party[guest]:
        print(f"{guest} doesn't have the {meal} in his/her collection.")

    else:
        party[guest].remove(meal)
        print(f"{guest} doesn't like the {meal}.")
        counter += 1

    return party, counter


party = {}
unliked_meals = 0

while True:
    command = input()
    if command == "Stop":
        for key, value in party.items():
            print(key + ": " + ', '.join(value))

        print(f"Unliked meals: {unliked_meals}")
        break

    current_command, guest, meal = command.split("-")

    if current_command == "Like":
        party = like(party, guest, meal)

    elif current_command == "Dislike":
        party , unliked_meals = dislike(party, guest, meal, unliked_meals)

