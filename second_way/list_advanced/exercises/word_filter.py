def length_is_even(current_products):
    return [text for text in current_products if len(text) % 2 == 0]


products = input().split()
print("\n".join(length_is_even(products)))