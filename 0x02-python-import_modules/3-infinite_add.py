#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    summer = 0
    for i in range(1, len(argv)):
        summer += int(argv[i])
    print("{}".format(summer))
