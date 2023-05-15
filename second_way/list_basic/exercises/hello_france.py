items = [item.split("->") for item in input().split("|")]
budget = float(input())
items_max_price = {"Clothes": 50, "Shoes": 35, "Accessories": 20.50}
train_ticket, higher_price = 150, 1.40
new_budget = []
profit = 0

for item, price in items:
    if float(price) <= items_max_price[item]:
        if budget - float(price) >= 0:
            budget -= float(price)
            new_budget.append(f"{float(price) * higher_price:.2f}")
            profit += float(price) * (higher_price - 1)

print(f"{' '.join(new_budget)}\nProfit: {profit:.2f}")
print(f"Hello, France!") if sum(map(float, new_budget)) + budget >= train_ticket else print("Not enough money.")
