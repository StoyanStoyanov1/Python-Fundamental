import re

pattern = r">>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)"
products = []
prices = []

while True:

    current_information = input()
    if current_information == "Purchase":
        break

    found_pattern = re.search(pattern, current_information)
    if found_pattern:
        product, price, quantity = found_pattern.groups()
        products.append(product)
        prices.append(float(price) * int(quantity))

print("Bought furniture:")

if products:
    print("\n".join(products))

print(f"Total money spend: {sum(prices):.2f}")
