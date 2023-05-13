budget = float(input())
price_kg_flour = float(input())
price_pack_eggs = price_kg_flour * 0.75
price_litter_milk = price_kg_flour * 1.25 * 0.250
total_price = price_kg_flour + price_pack_eggs + price_litter_milk

colored_eggs = 0
number_of_loaves = 0
while True:
    if budget - total_price < 0:
        print(f"You made {number_of_loaves} loaves of Easter bread! "
              f"Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
        break

    budget -= total_price
    number_of_loaves += 1
    colored_eggs += 3
    if number_of_loaves % 3 == 0:
        colored_eggs -= (number_of_loaves - 2)
