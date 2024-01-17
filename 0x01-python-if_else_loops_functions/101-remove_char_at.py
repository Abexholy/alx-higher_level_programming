#!/usr/bin/python3
def remove_char_at(str, n):
    abbey = ''
    j = 0
    for char in str:
        if j != n:
            abbey += str[j]
        j += 1
    return (abbey)
