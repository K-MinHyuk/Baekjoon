from collections import deque
import sys

def func(st, dq, depth):
    if st[:4] == 'push':
        dq.append(int(st.split()[-1]))
        depth += 1
    elif st == 'pop':
        if depth == 0:
            print(-1)
        else:
            print(dq.pop())
            depth -= 1
    elif st == 'size':
        print(depth)
    elif st == 'empty':
        if depth == 0:
            print(1)
        else:
            print(0)
    elif st == 'top':
        if depth == 0:
            print(-1)
        else:
            print(dq[-1])
    return dq, depth

if __name__ == '__main__':
    n = int(input())
    stack = deque()
    depth = 0
    for i in range(n):
        string = sys.stdin.readline().strip()
        stack, depth = func(string, stack, depth)
