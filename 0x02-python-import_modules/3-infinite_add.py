#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    add = 0

    for num in range(len(sys.argv) - 1):
        add += int(sys.argv[num + 1])
    print("{:d}".format(add))
