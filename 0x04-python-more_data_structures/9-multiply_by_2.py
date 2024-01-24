#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    my_dic = a_dictionary.copy()
    list_all = list(my_dic.keys())

    for j in list_all:
        my_dic[j] *= 2

    return (my_dic)
