def shoot_for_the_win(shot_targets, command):
    counter = 0
    while command != "End":
        index = int(command)
        if index < len(shot_targets) and shot_targets[index] != -1:
            counter += 1
            shot = shot_targets[index]
            for the_index in range(len(shot_targets)):
                if the_index != index and shot_targets[the_index] != -1:
                    if shot_targets[the_index] > shot:
                        shot_targets[the_index] -= shot

                    else:
                        shot_targets[the_index] += shot
            shot_targets[index] = -1
        command = input()

    shot_targets = [str(target) for target in shot_targets]

    return f'Shot targets: {counter} -> {" ".join(shot_targets)}'


targets = list(map(int, input().split()))
the_command = input()
print(shoot_for_the_win(targets, the_command))
