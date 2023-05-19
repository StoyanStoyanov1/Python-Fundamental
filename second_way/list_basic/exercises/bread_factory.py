def rest(energy, current_energy):
    """You gain energy (the number in the second part). Note: your energy cannot exceed your initial energy
(100). Print: "You gained {gained_energy} energy.".
o After that, print your current energy: "Current energy: {current_energy}."""
    energy += current_energy
    if energy > 100:
        current_energy = current_energy - energy + 100
        energy = 100

    print(f"You gained {current_energy} energy.\nCurrent energy: {energy}.")
    return energy


def order(coins, energy, current_coins):
    """You've earned some coins (the number in the second part).
o Each time you get an order, your energy decreases by 30 points.
▪ If you have the energy to complete the order, print: "You earned {earned} coins.".
▪ Otherwise, skip the order and gain 50 energy points. Print: "You had to rest!"."""

    if energy >= 30:
        energy -= 30
        coins += current_coins
        print(f"You earned {current_coins} coins.")

    else:
        energy += 50
        print("You had to rest!")
    return energy, coins


def any_other_case(coins, price, item):
    """o If you have enough money, you should buy the ingredient and print:
"You bought {ingredient}."
o Otherwise, print "Closed! Cannot afford {ingredient}." and your bakery rush is over. """

    coins -= price
    print(f"You bought {item}.")

    return coins


energy, coins = 100, 100
events = [event.split("-") for event in input().split("|")]

completed = True

for event, value in events:
    if event == "rest":
        current_energy = int(value)
        energy = rest(energy, current_energy)

    elif event == "order":
        current_coins = int(value)
        energy, coins = order(coins, energy, current_coins)

    else:
        price = int(value)
        if coins >= price:
            coins = any_other_case(coins, price, event)
        else:
            print(f"Closed! Cannot afford {event}.")
            completed = False
            break

if completed:
    print(f"Day completed!\nCoins: {coins}\nEnergy: {energy}")
