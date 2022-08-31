#!/usr/bin/python3
from add_0 import add

if __name__ == "__main__":
    import sys
    a = 1
    b = 2
    c = add(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, c))
