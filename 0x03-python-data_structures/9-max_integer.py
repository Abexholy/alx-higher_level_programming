#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) <= 0:
        return None
    else:
       my_maximum = my_list[0]
       for i in rang(len(my_list)):
           if my_list[i] > my_maximum:
              my_ maximum = my_list[i]
        return my_maximum
