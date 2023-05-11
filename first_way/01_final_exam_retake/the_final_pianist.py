def add(collection, piece, composer, key):
    if piece not in collection:
        collection[piece] = {"Composer": composer, "Key": key}
        print(f'{piece} by {composer} in {key} added to the collection!')
    else:
        print(f"{piece} is already in the collection!")


def remove(collection, piece):
    if piece in collection:
        print(f"Successfully removed {piece}!")
        del collection[piece]
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")


def change_key_all(collection, piece, new_key):
    if piece in collection:
        collection[piece]["Key"] = new_key
        print(f"Changed the key of {piece} to {new_key}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")


def result(collection):
    for piece in collection.keys():
        print(f"{piece} -> Composer: {collection[piece]['Composer']}, Key: {collection[piece]['Key']}")


def the_pianist_logic(number_of_pieces):
    collection = {}

    for _ in range(number_of_pieces):
        piece, composer, key = input().split("|")
        collection[piece] = {"Composer": composer, "Key": key}

    while True:
        command = input().split("|")
        if command[0] == "Stop":
            result(collection)
            break

        elif command[0] == "Add":
            piece, composer, key = command[1], command[2], command[3]
            add(collection, piece, composer, key)

        elif command[0] == "Remove":
            piece = command[1]
            remove(collection, piece)

        elif command[0] == "ChangeKey":
            piece, new_key = command[1], command[2]
            change_key_all(collection, piece, new_key)



number_of_pieces = int(input())
the_pianist_logic(number_of_pieces)

