def messaging (sum_of_numbers, the_text):
    """
    ### That is the Function "messaging" ###

I am looking for the Index which is the sum of the numbers,
if the sum of the numbers is greater than the length of the text,
then I keep counting until it reaches the sum of the numbers and the given index
I remove it and save it. After going through all the numbers I return the result"""

    result = []
    for number in sum_of_numbers:
        sum_number = [int(digit) for digit in number]
        return_letter = the_text.pop(sum(sum_number) - (len(the_text)))
        result.append(return_letter)

    return "".join(result)


numbers = input().split()
text = [letter for letter in input()]
print(messaging(numbers, text))
