from functools import reduce


def reduce_my_list(list):
    return reduce(lambda a, b: a + b, list)


print(reduce_my_list([1, 2, 3, 4, 5, 6, 7]))

