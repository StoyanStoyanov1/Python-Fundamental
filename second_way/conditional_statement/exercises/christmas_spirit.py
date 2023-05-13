quantity_of_decorations = int(input())
days_left_until_christmas = int(input())

decoration = {"Ornament Set": {"Price": 2, "Points": 5},
              "Tree Skirt": {"Price": 5, "Points": 3},
              "Tree Garland": {"Price": 3, "Points": 10},
              "Tree Lights": {"Price": 15, "Points": 17}}

budget = 0
total_spirit = 0

for day in range(1, days_left_until_christmas + 1):
    sum_for_a_day = 0

    if day % 11 == 0:
        quantity_of_decorations += 2

    if day % 2 == 0:
        sum_for_a_day += decoration["Ornament Set"]["Price"] * quantity_of_decorations
        total_spirit += decoration["Ornament Set"]["Points"]

    if day % 3 == 0:
        sum_for_a_day += (decoration["Tree Skirt"]["Price"] + decoration["Tree Garland"]["Price"]) \
                         * quantity_of_decorations
        total_spirit += decoration["Tree Skirt"]["Points"] + decoration["Tree Garland"]["Points"]

    if day % 5 == 0:
        sum_for_a_day += decoration["Tree Lights"]["Price"] * quantity_of_decorations
        total_spirit += decoration["Tree Lights"]["Points"]
        if day % 3 == 0:
            total_spirit += 30

    if day % 10 == 0:
        total_spirit -= 20
        sum_for_a_day += decoration["Tree Skirt"]["Price"] + decoration["Tree Garland"]["Price"] \
                         + decoration["Tree Lights"]["Price"]

    if day == days_left_until_christmas and day % 10 == 0:
        total_spirit -= 30

    budget += sum_for_a_day

print(f"Total cost: {budget}\nTotal spirit: {total_spirit}")
