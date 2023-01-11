from collections import deque
import sys




n = int(input())
dq = deque()
for i in range(n):
    line = sys.stdin.readline().strip().split(' ')

    if line[0] == 'push_front':
        dq.appendleft(int(line[1]))
    elif line[0] == 'push_back':
        dq.append(int(line[1]))
    elif line[0] == 'pop_front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())
    elif line[0] == 'pop_back':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.pop())
    elif line[0] == 'size':
        print(len(dq))
    elif line[0] == 'empty':
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif line[0] == 'front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    elif line[0] == 'back':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])