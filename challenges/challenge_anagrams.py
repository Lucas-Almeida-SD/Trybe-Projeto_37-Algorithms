def split_list(my_list, start_list, end_list):
    pivot = my_list[end_list]
    delimiter = start_list

    for index in range(start_list, end_list):
        if my_list[index] <= pivot:
            current = my_list[delimiter]
            my_list[delimiter] = my_list[index]
            my_list[index] = current
            delimiter += 1

    my_list[delimiter], my_list[end_list] = pivot, my_list[delimiter]

    return delimiter


def sort_string(my_list, start_list, end_list):
    if start_list < end_list:
        index_pivot = split_list(my_list, start_list, end_list)
        sort_string(my_list, start_list, index_pivot - 1)
        sort_string(my_list, index_pivot + 1, end_list)


def is_anagram(first_string: str, second_string: str):
    if first_string == second_string == "":
        return (first_string, second_string, False)

    lower_first_string = list(first_string.lower())
    lower_second_string = list(second_string.lower())

    sort_string(lower_first_string, 0, len(lower_first_string) - 1)
    sort_string(lower_second_string, 0, len(lower_second_string) - 1)

    return (
        "".join(lower_first_string),
        "".join(lower_second_string),
        lower_first_string == lower_second_string,
    )
