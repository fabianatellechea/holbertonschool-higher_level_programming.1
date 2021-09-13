#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv) - 1

    if argc == 1:
        print("{:d} argument:".format(argc))
        for arg in sys.argv[1:]:
            print("{:d}: {}".format(argc, arg))
    if argc == 0:
        print("0 arguments.")
        for arg in sys.argv[1:]:
            print("{:d}: {}".format(argc, arg))
    elif argc > 1:
        print("{:d} arguments:".format(argc))
        for arg in range(len(sys.argv[1:])):
            print("{:d}: {}".format(arg + 1, sys.argv[1:][arg]))
