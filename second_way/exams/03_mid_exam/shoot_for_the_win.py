class ShootForTheWin:

    def __init__(self, targets, shoots):
        self.targets = targets
        self.shoots = shoots
        self.shoots_targets = self.shoots_targets()

    def shoot_a_target(self, current_target):
        for target_index in range(len(self.targets)):
            if self.targets[target_index] != -1:
                if self.targets[target_index] > current_target:
                    self.targets[target_index] -= current_target
                else:
                    self.targets[target_index] += current_target

    def shoots_targets(self):
        shoots_targets = 0
        for shoot in self.shoots:
            if shoot in range(len(self.targets)):
                if self.targets[shoot] != -1:
                    shoots_targets += 1
                    current_target = self.targets[shoot]
                    self.targets[shoot] = -1
                    self.shoot_a_target(current_target)

        return shoots_targets

    def __repr__(self):
        return f"Shot targets: {self.shoots_targets} -> {' '.join(str(target) for target in self.targets)}"


targets = list(map(int, input().split()))
shoots = []

while True:
    shoot = input()
    if shoot.isdigit():
        shoots.append(int(shoot))
    else:
        break

print(ShootForTheWin(targets, shoots))
