def print_odd_numbers(lst):
    if len(lst) == 0:
        return
    if lst[0] % 2 != 0:
        print(lst[0])
    print_odd_numbers(lst[1:])


print_odd_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])


def count_list_elements(lst):
    if len(lst) == 0:
        return 0
    else:
        return 1 + count_list_elements(lst[1:])


print(count_list_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


def next_element(lst):
    index = [0]

    def get_next():
        result = None
        if index[0] < len(lst):
            result = lst[index[0]]
            index[0] += 1
        return result

    return get_next


next_list_element = next_element([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(next_list_element())
print(next_list_element())
print(next_list_element())
print(next_list_element())
print(next_list_element())
