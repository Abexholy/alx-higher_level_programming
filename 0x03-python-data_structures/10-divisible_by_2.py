#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    longe = len(my_list)
    old_list = []
    for i in range(longe):
        if my_list[i] % 2 == 0:
            old_list.append(True)
        else:
            old_list.append(False)
    return old_list
