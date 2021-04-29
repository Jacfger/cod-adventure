import numpy as np
import collections

def p1(string):
    x = collections.Counter(string)
    down = x[')']
    up = x['(']
    print(up - down)

def p2(string):
    pos = 1
    floor = 0
    for c in string:
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1
        if floor == -1:
            print(pos)
            break
        else:
            pos += 1

if __name__ == '__main__':
    with open('day1.input', 'r') as f:
        string = f.read()
    # main(string) # rename function p1 or p2 to main