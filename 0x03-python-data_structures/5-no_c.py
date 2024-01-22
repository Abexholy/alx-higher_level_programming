#!/usr/bin/python3
def no_c(my_string):
    if my_string[:]:
        ab_string = my_string.translate({ord("c"): None})
        bol_string = ab_string.translate({ord("C"): None})
        return bol_string
    return my_string
