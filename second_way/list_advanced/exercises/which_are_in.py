def which_are_in(current_list, current_new_list):
    for index in range(len(current_list) - 1, -1, -1):
        word = current_list[index]
        word_in_new_list = False
        for new_word in current_new_list:
            if word in new_word:
                word_in_new_list = True
        if not word_in_new_list:
            current_list.remove(word)

    return current_list


the_list, new_list = input().split(", "), input().split(", ")
print(which_are_in(the_list, new_list))
