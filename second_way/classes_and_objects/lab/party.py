class Party:
    def __init__(self):
        self.people = []


party = Party()

while True:
    name = input()
    if name == "End":
        break

    party.people.append(name)

print("Going:", ", ".join(party.people))
print("Total:", len(party.people))
