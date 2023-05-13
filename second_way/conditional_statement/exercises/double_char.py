while True:
    text = input()
    if text == "End":
        break

    if text != "SoftUni":
        print("".join([char * 2 for char in text]))
