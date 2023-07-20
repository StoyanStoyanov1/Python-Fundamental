class ThePianist:

    def __init__(self, number_of_pieces):
        self.number_of_pieces = number_of_pieces
        self.pieces = self.current_pieces()
        self.commands()

    def current_pieces(self):
        current_pieces = {}
        for _ in range(self.number_of_pieces):
            piece, composer, key = input().split("|")
            current_pieces[piece] = {"Composer": composer, "Key": key}

        return current_pieces

    def add_the_given_piece(self, piece, composer, key):
        if piece not in self.pieces:
            self.pieces[piece] = {"Composer": composer, "Key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")

        else:
            print(f"{piece} is already in the collection!")

    def remove_the_given_piece(self, piece):
        if piece in self.pieces:
            del self.pieces[piece]
            print(f"Successfully removed {piece}!")

        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    def change_key(self, piece, new_key):
        if piece in self.pieces:
            self.pieces[piece]["Key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    def commands(self):

        while True:
            command = input().split("|")
            if command[0] == "Stop":
                break

            if command[0] == "Add":
                self.add_the_given_piece(command[1], command[2], command[3])

            elif command[0] == "Remove":
                self.remove_the_given_piece(command[1])

            elif command[0] == "ChangeKey":
                self.change_key(command[1], command[2])

    def all_pieces(self):
        all_pieces = []
        for piece, info in self.pieces.items():
            all_pieces.append(f"{piece} -> Composer: {info['Composer']}, Key: {info['Key']}")

        return all_pieces

    def __repr__(self):
        return '\n'.join(self.all_pieces())


print(ThePianist(int(input())))
