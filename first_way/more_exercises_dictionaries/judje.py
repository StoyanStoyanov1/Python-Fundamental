result = {}

while True:
    command = input()
    if command == "no more time":
        break

    command = command.split(" -> ")
    username, contest, points = command[0], command[1], int(command[2])

    if contest not in result:
        result[contest] = {username: points}
    elif username not in result[contest]:
        result[contest][username] = points
    elif points > result[contest][username]:
        result[contest][username] = points

individual_standings = {}

for contest, username in result.items():
    print(f"{contest}: {len(username)} participants")
    counter = 0
    for index in range(len(username)):
        counter += 1
        sorted_points = sorted(username.items(), key=lambda sort: (-sort[1], sort[0]))
        print(f"{counter}. {sorted_points[index][0]} <::> {sorted_points[index][1]}")
        if sorted_points[index][0] not in individual_standings:
            individual_standings[sorted_points[index][0]] = sorted_points[index][1]
        else:
            individual_standings[sorted_points[index][0]] += sorted_points[index][1]

sorted_individual_standings = sorted(individual_standings.items(), key=lambda points: (-points[1], points[0]))

print("Individual standings:")

counter = 0

for index in range(len(sorted_individual_standings)):
    counter += 1
    print(f"{counter}. {sorted_individual_standings[index][0]} -> {sorted_individual_standings[index][1]}")
