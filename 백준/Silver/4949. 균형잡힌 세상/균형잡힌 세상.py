from collections import deque
import sys

while True:
    flg = 0
    br = deque()
    string = sys.stdin.readline()
    if string == '.\n':
        break
    for s in string:
        if s == '(' or s == '[':
            br.append(s)
        elif s == ')' or s == ']':
            if len(br) == 0:
                flg = 1
            elif br[-1] == '[' and s == ']':
                _ = br.pop()
            elif br[-1] == '(' and s == ')':
                _ = br.pop()
            else:
                flg = 1
    if flg or len(br) != 0:
        print('no')
    else:
        print('yes')
