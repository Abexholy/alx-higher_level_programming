#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    numbs = 0

    for j in range(x):
        try:
            print("{:d}".format(my_list[j]), end='')
        except TypeError:
            pass
        except ValueError:
            pass
        else:
            numbs += 1

    print()
    return (numbs)
