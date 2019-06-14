def filter_division_8(my_list):
    return list(filter(lambda x: x % 8 == 0, my_list))


print(filter_division_8([0, 1, 8, 16, 54, 34, 12, 45, 64]))
