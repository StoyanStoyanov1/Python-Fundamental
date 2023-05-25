def add_lesson(list_of_lesson, lesson_title):
    if not lesson_title in list_of_lesson:
        list_of_lesson.append(lesson_title)
    return list_of_lesson


def insert_lesson(list_of_lesson, lesson_title, index):
    if not lesson_title in list_of_lesson:
        list_of_lesson.insert(int(index), lesson_title)
    return list_of_lesson


def remove_lesson(list_of_lesson, lesson_title):
    if lesson_title in list_of_lesson:
        lesson_position = list_of_lesson.index(lesson_title)
        if lesson_position + 1 in range(len(list_of_lesson)):
            if "Exercise" in list_of_lesson[lesson_position + 1]:
                list_of_lesson.pop(lesson_position + 1)
        list_of_lesson.pop(lesson_position)
    return list_of_lesson


def swap_lesson(list_of_lesson, first_lesson_title, second_lesson_title):
    if first_lesson_title in list_of_lesson and second_lesson_title in list_of_lesson:
        first_position = list_of_lesson.index(first_lesson_title)
        second_position = list_of_lesson.index(second_lesson_title)
        first_has_exercise = False
        second_has_exercise = False
        if first_position + 1 in range(len(list_of_lesson)):
            first_has_exercise = "Exercise" in list_of_lesson[first_position + 1]
        if second_position + 1 in range(len(list_of_lesson)):
            second_has_exercise = "Exercise" in list_of_lesson[second_position + 1]
        list_of_lesson[first_position], list_of_lesson[second_position] = \
            list_of_lesson[second_position], list_of_lesson[first_position]
        if first_has_exercise and second_has_exercise:
            list_of_lesson[first_position + 1], list_of_lesson[second_position + 1] = \
                list_of_lesson[second_position + 1], list_of_lesson[first_position + 1]
        elif not first_has_exercise and second_has_exercise:
            list_of_lesson.insert(first_position + 1, list_of_lesson.pop(second_position + 1))
        elif first_has_exercise and not second_has_exercise:
            list_of_lesson.insert(second_position + 1, list_of_lesson.pop(first_position + 1))

    return list_of_lesson


def exercise_lesson(list_of_lesson, lesson_title):
    if lesson_title in list_of_lesson and f"{lesson_title}-Exercise" not in list_of_lesson:
        lesson_index = list_of_lesson.index(lesson_title)
        list_of_lesson.insert(lesson_index + 1, f"{lesson_title}-Exercise")
    elif lesson_title not in list_of_lesson:
        list_of_lesson.append(lesson_title)
        list_of_lesson.append(f"{lesson_title}-Exercise")

    return list_of_lesson


the_list = input().split(', ')
command = input().split(":")

while command[0] != "course start":
    typ_lesson = command[0]
    title_lesson = command[1]
    if len(command) > 2:
        index_lesson = command[2]
        if typ_lesson == "Insert":
            insert_lesson(the_list, title_lesson, index_lesson)
        elif typ_lesson == "Swap":
            swap_lesson(the_list, title_lesson, index_lesson)


    elif typ_lesson == "Add":
        add_lesson(the_list, title_lesson)
    elif typ_lesson == "Remove":
        remove_lesson(the_list, title_lesson)
    elif typ_lesson == "Exercise":
        exercise_lesson(the_list, title_lesson)

    command = input().split(":")

for counter, text in enumerate(the_list):
    print(f'{counter + 1}.{text}')
