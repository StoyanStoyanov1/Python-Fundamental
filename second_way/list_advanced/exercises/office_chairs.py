def office_chairs(current_rooms, current_chairs):
    free_chairs = 0
    result = []
    index = 0
    for room in range(1, current_rooms + 1):
        count_chairs = len(current_chairs[index][0])
        needed_chairs = int(current_chairs[index][1])
        if count_chairs > needed_chairs:
            free_chairs += count_chairs - needed_chairs

        elif count_chairs < needed_chairs:
            more_chairs = needed_chairs - count_chairs
            result.append(f"{more_chairs} more chairs needed in room {room}")

        index += 1
    if result:
        return "\n".join(result)
    else:
        return f"Game On, {free_chairs} free chairs left"


number_of_rooms = int(input())
chairs = [input().split() for _ in range(number_of_rooms)]

print(office_chairs(number_of_rooms, chairs))
