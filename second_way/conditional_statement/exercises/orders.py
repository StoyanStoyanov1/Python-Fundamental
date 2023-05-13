number_of_orders = int(input())
total_price = 0

for _ in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if days not in range(1, 32):
        continue

    if not 0.01 <= price_per_capsule <= 100:
        continue

    if capsules_per_day not in range(1, 2001):
        continue

    price_order = price_per_capsule * days * capsules_per_day
    total_price += price_order
    print(f"The price for the coffee is: ${price_order:.2f}")

print(f"Total: ${total_price:.2f}")
