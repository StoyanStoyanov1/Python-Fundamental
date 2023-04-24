MAX_PEOPLE_ON_LIFT = 4

number_of_waiting_people = int(input())
current_lift = list(map(int, input().split()))
empty_spots = False

for index in range(len(current_lift)):

    while current_lift[index] < MAX_PEOPLE_ON_LIFT and number_of_waiting_people > 0:
        current_lift[index] += 1
        number_of_waiting_people -= 1

    if number_of_waiting_people == 0 and current_lift[index] < MAX_PEOPLE_ON_LIFT:
        empty_spots = True
        break

result = [str(lift) for lift in current_lift]

if empty_spots:
    print(f"The lift has empty spots!\n{' '.join(result)}")
elif number_of_waiting_people > 0:
    print(f"There isn't enough space! {number_of_waiting_people} people in a queue!\n{' '.join(result)}")
else:
    print(' '.join(result))
