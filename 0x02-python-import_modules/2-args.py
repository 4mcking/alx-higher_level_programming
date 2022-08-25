#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    w = len(argv)
    print("{:d} {:s}{:s}".format(w - 1, "argument" if w <= 2 else "arguments",
                                 "." if w == 1 else ":"))
    for i, s in enumerate(argv):
        if i > 0:
            print("{:d}: {:s}".format(i, s))
