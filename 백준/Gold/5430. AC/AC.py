import sys
from collections import deque

n = int(input())
for i in range(n):
    start = True
    flg = True
    line = sys.stdin.readline().strip()
    m = int(sys.stdin.readline().strip())
    if m == 0:
        arr = sys.stdin.readline().strip()
        arr = []
    else:
        arr = deque(map(int, sys.stdin.readline().strip()[1:-1].split(',')))
    for j in line:
        if j == 'R':
            start = not start
        if j == 'D':
            if len(arr) == 0:
                print('error')
                flg = not flg
                break
            else:
                if start:
                    arr.popleft()
                else:
                    arr.pop()
    if flg:
        if not start:
            arr.reverse()
        print('[',end='')
        print(*arr, sep=',',end='')
        print(']')

            