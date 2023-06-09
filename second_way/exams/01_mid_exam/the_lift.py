class TheLift:
    __max_state_on_the_lift = 4

    def __init__(self, people, state_on_the_lift):
        self.people = people
        self.state_on_the_lift = state_on_the_lift
        self.result = self.result()

    def result(self):
        for index in range(len(self.state_on_the_lift)):
            current_state_of_the_lift = self.state_on_the_lift.pop(index)
            while current_state_of_the_lift < self.__max_state_on_the_lift and self.people:
                self.people -= 1
                current_state_of_the_lift += 1

            self.state_on_the_lift.insert(index, current_state_of_the_lift)

            if current_state_of_the_lift < self.__max_state_on_the_lift:
                return "The lift has empty spots!"

        if self.people:
            return f"There isn't enough space! {self.people} people in a queue!"

    def __repr__(self):
        return f"{self.result}\n{' '.join(str(x) for x in self.state_on_the_lift)}" if self.result \
            else ' '.join(str(x) for x in self.state_on_the_lift)


people = int(input())
state_on_the_lift = list(map(int, input().split()))

print(TheLift(people, state_on_the_lift))