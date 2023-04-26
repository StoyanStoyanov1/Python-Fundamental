def best_candidate(current_submissions):
    best_points = 0
    candidate = ""

    for submission, points in current_submissions.items():

        if sum(points.values()) > best_points:
            best_points = sum(points.values())
            candidate = submission

    return f"Best candidate is {candidate} with total {best_points} points."


def contests():
    current_contests = {}

    while True:
        command = input()
        if ":" not in command:
            break

        contest, password = command.split(":")

        current_contests[contest] = {"Password": password}

    return current_contests


def submissions(current_contests):
    current_submissions = {}

    while True:
        command = input()
        if "=>" not in command:
            break

        command = command.split("=>")
        contest, password, username, points = command[0], command[1], command[2], int(command[3])
        if contest in current_contests and password == current_contests[contest]["Password"]:
            if username not in current_submissions:
                current_submissions[username] = {contest: points}
            else:
                if contest not in current_submissions[username]:
                    current_submissions[username][contest] = points

                elif current_submissions[username][contest] < points:
                    current_submissions[username][contest] = points

    return current_submissions


def ranking(current_submissions):
    print("Ranking:")

    for submission, contest in sorted(current_submissions.items()):
        print(submission)
        for index in range(len(contest)):
            sorted_contest = sorted(contest.items(), key=lambda con: con[1], reverse=True)
            print(f"#  {sorted_contest[index][0]} -> {sorted_contest[index][1]}")


current_contests = contests()
current_submissions = submissions(current_contests)
print(best_candidate(current_submissions))
ranking(current_submissions)
