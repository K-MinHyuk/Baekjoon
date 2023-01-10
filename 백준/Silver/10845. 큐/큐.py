from collections import deque
import sys
n = int(input())
Q = deque()
depth = 0
for i in range(n):
    string = list(sys.stdin.readline().strip().split())
    if string[0] == 'push':
        Q.append(int(string[1]))       
    elif string[0] == 'pop':
        if len(Q) == 0:
            print(-1)
        else:
            print(Q.popleft())
    elif string[0] == 'size':
        print(len(Q))
    elif string[0] == 'empty':
        if len(Q) == 0:
            print(1)
        else:
            print(0)
    elif string[0] == 'front':
        if len(Q) == 0:
            print(-1)
        else:
            print(Q[0])
    elif string[0] == 'back':
        if len(Q) == 0:
            print(-1)
        else:
            print(Q[-1])