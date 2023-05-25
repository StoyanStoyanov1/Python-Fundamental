def pokemon_go(sequence_of_integers):
    result = 0
    while len(sequence_of_integers) > 0:
        the_index = int(input())
        add_result = 0
        if the_index < 0:
            add_result += sequence_of_integers[0]
            sequence_of_integers[0] = sequence_of_integers[-1]

        elif the_index >= len(sequence_of_integers):
            add_result += sequence_of_integers[-1]
            sequence_of_integers[-1] = sequence_of_integers[0]
        else:
            add_result += sequence_of_integers.pop(the_index)
        result += add_result

        for index, number in enumerate(sequence_of_integers):
            if add_result < number:
                sequence_of_integers[index] -= add_result
            else:
                sequence_of_integers[index] += add_result

    return result


the_numbers = list(map(int, input().split()))
print(pokemon_go(the_numbers))
