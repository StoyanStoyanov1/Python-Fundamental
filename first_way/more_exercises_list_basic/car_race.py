def car_care (total_time):
    """
    ### That is Function car_race ###

I divide the numbers as time into left and right cars,
the indices I get are always odd because the middle is the
finish of the race. The right car starts from the first index
to the end point which is the middle and the left car starts
from the last index.

I return the winner with less time
    """
    left_car = [total_time[sec] for sec in range(len(total_time) // 2)]
    left_car_time = 0
    right_car = [total_time[sec] for sec in range(-1,-len(total_time) // 2, -1)]
    right_car_time = 0
    for time in left_car:
        if time != 0:
            left_car_time += time
        else:
            left_car_time *= 0.8
    for time in right_car:
        if time != 0:
            right_car_time += time
        else:
            right_car_time *= 0.8

    return f"The winner is left with total time: {left_car_time:.1f}" \
        if left_car_time < right_car_time \
        else f"The winner is right with total time: {right_car_time:.1f}"


numbers = list(map(int, input().split()))

print(car_care(numbers))