def password_validator(current_password):
    password_is_not_valid = []

    if len(current_password) not in range(6, 11):
        password_is_not_valid.append("Password must be between 6 and 10 characters")

    digits = [digit for digit in current_password if digit.isdigit()]
    other_symbol = list(map(lambda symbol: not (symbol.isdigit() or symbol.isalpha()), current_password))

    if True in other_symbol:
        password_is_not_valid.append("Password must consist only of letters and digits")

    if len(digits) < 2:
        password_is_not_valid.append("Password must have at least 2 digits")

    if password_is_not_valid:
        return "\n".join(password_is_not_valid)

    else:
        return "Password is valid"


password = input()
print((password_validator(password)))
