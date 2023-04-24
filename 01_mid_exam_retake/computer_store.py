total_price = 0
taxes = 0
special = 1

while True:
    command = input()

    if command == "special":
        taxes = total_price * 0.20
        special -= 0.1
        break

    elif command == "regular":
        taxes = total_price * 0.20
        break

    price = float(command)
    if price < 0:
        print("Invalid price!")
        continue

    total_price += price

if total_price > 0:
    print(f"Congratulations you've just bought a new computer!\nPrice without " 
          f"taxes: {total_price:.2f}$\nTaxes: {taxes:.2f}$\n-----------\n"
          f"Total price: {(total_price + taxes) * special:.2f}$")

else:
    print("Invalid order!")
