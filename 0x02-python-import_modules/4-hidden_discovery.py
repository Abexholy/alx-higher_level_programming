#!/usr/bin/python3
if __name__ == "__main":
    from hidden_4 import *
    mmyf = dir()
    for i in range(0, len(mmyf)):
        if mmyf[i][:2] != "__":
            print("{:s}".format(mmyf[i]))
