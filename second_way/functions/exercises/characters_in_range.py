def characters_in_range(begin, end):
    return [chr(symbol) for symbol in range(begin + 1, end)]


first_symbol, second_symbol = ord(input()), ord(input())
print(" ".join(characters_in_range(first_symbol, second_symbol)))
