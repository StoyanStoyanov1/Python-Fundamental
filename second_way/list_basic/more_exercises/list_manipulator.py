from sys import maxsize


def exchange(index):
    """### EXCHANGE ###
            splits the list after the given index and exchanges the places of the two resulting sub-lists.
            1 -	If the index is outside the boundaries of the list, print "Invalid index"
            2 -	A negative index is considered invalid
             """

    if index in range(len(the_list)):
        left_list = the_list[:index + 1:]
        right_list = the_list[index + 1:]
        the_list.clear()
        the_list.extend(right_list), the_list.extend(left_list)
        return the_list

    return print('Invalid index')


def the_max_number(even_or_odd):
    """ ### MAX EVEN/ODD element ###
            returns the INDEX of the max even/odd element """

    max_number = -maxsize
    max_index = 0

    for index in range(len(the_list)):
        if even_or_odd == "even" and the_list[index] % 2 == 0 and the_list[index] >= max_number:
            max_number = the_list[index]
            max_index = index
        elif even_or_odd == "odd" and the_list[index] % 2 != 0 and the_list[index] >= max_number:
            max_number = the_list[index]
            max_index = index

    if max_number == -maxsize:
        return print('No matches')

    return print(max_index)


def the_min_number(even_or_odd):
    """ ### MIN EVEN/ODD element ###
            returns the INDEX of the min even/odd element"""

    max_number = maxsize
    max_index = 0

    for index in range(len(the_list)):
        if even_or_odd == "even" and the_list[index] % 2 == 0 and the_list[index] <= max_number:
            max_number = the_list[index]
            max_index = index
        elif even_or_odd == "odd" and the_list[index] % 2 != 0 and the_list[index] <= max_number:
            max_number = the_list[index]
            max_index = index

    if max_number == maxsize:
        return print('No matches')

    return print(max_index)


def first_elements(count, even_or_odd):
    """ ### FIRST COUNT EVEN OR ODD ###
            returns the first count even/odd elements. """

    if count in range(1, len(the_list) + 1):
        elements = []
        counter = 0
        for number in the_list:
            if even_or_odd == 'even' and number % 2 == 0:
                elements.append(number)
                counter += 1
            elif even_or_odd == 'odd' and number % 2 != 0:
                elements.append(number)
                counter += 1
            if counter == count:
                break

        return print(elements)

    return print('Invalid count')


def last_elements(the_list, count, even_or_odd):
    """ ### LAST COUNT EVEN OR ODD ###
            returns the last count even/odd elements. """

    the_list = the_list[::-1]
    if count in range(1, len(the_list) + 1):
        elements = []
        counter = 0

        for number in the_list:
            if even_or_odd == 'even' and number % 2 == 0:
                elements.append(number)
                counter += 1
            elif even_or_odd == 'odd' and number % 2 != 0:
                elements.append(number)
                counter += 1
            if counter == count:
                break

        return print(elements[::-1])

    return print("Invalid count")


the_list = list(map(int, input().split()))
command = input()

while command != 'end':
    command = command.split()
    if command[0] == "exchange":
        the_index = int(command[1])
        exchange(the_index)
    elif command[0] == 'max':
        even_odd = command[1]
        the_max_number(even_odd)
    elif command[0] == 'min':
        even_odd = command[1]
        the_min_number(even_odd)
    elif command[0] == 'first':
        the_count = int(command[1])
        even_odd = command[2]
        first_elements(the_count, even_odd)
    elif command[0] == 'last':
        the_count = int(command[1])
        even_odd = command[2]
        last_elements(the_list, the_count, even_odd)
    command = input()

print(the_list)
