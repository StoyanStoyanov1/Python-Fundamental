def decipher_this(secret_message):
    message = []
    for word in secret_message:
        letters = []
        number = ""
        for symbol in word:
            if symbol.isdigit():
                number += symbol
            else:
                letters.append(symbol)

        letters[0], letters[-1] = letters[-1], letters[0]
        new_word = chr(int(number)) + "".join(letters)

        message.append(new_word)

    return " ".join(message)


text = input().split()
print(decipher_this(text))

