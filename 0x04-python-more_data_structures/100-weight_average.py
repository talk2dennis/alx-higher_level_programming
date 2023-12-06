#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    total = 0
    value = 0

    for num in my_list:
        total += (num[0] * num[1])
        value += num[1]
    return total / value
