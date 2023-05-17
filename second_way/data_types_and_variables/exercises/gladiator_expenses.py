lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

expenses = 0
shield_is_broken = False

for lost_fight in range(1, lost_fights_count + 1):
    if lost_fight % 2 == 0:
        expenses += helmet_price

    if lost_fight % 3 == 0:
        expenses += sword_price

    if lost_fight % 2 == 0 and lost_fight % 3 == 0:
        expenses += shield_price
        if shield_is_broken:
            expenses += armor_price
            shield_is_broken = False
        else:
            shield_is_broken = True

print(f"Gladiator expenses: {expenses:.2f} aureus")
