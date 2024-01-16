#!/usr/bin/python3
for first_figure in range(0, 10):
    for second_figure in range(first_figure + 1, 10):
        if first_figure == 8 and second_figure == 9:
            print("{}{}".format(first_figure, second_figure))
        else:
            print("{}{}, ".format(first_figure, second_figure), end='')
