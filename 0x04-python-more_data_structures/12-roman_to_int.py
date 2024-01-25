#!/usr/bin/python3
def to_subtract(list_num):
    total_sub = 0
    maximum_list = max(list_num)

    for i in list_num:
        if maximum_list > i:
            total_sub += i

    return (maximum_list - total_sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    roar_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(roar_n.keys())

    num = 0
    last_rom = 0
    list_num = [0]

    for ch in roman_string:
        for r_num in list_keys:
            if r_num == ch:
                if roar_n.get(ch) <= last_rom:
                    num += to_subtract(list_num)
                    list_num = [roar_n.get(ch)]
                else:
                    list_num.append(roar_n.get(ch))

                last_rom = roar_n.get(ch)

    num += to_subtract(list_num)

    return (num)
