#!/usr/bin/python3

def magic_calculation(a, b):
    answ = 0
    for j in range(1, 3):
        try:
            if j > a:
                raise Exception("Too far")
            else:
                answ += a ** b / j
        except Exception:
            answ = b + a
            break
    return answ
