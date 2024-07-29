def split_list(input_list):

    n = len(input_list)

    if n == 0:
        return [[], []]

    mid_point = (n + 1) // 2

    list1 = input_list[:mid_point]
    list2 = input_list[mid_point:]
    return [list1, list2]


print(split_list([1, 2, 3, 4, 5, 6]))
print(split_list([1, 2, 3]))
print(split_list([1, 2, 3, 4, 5]))
print(split_list([1]))
print(split_list([]))