from collections import deque
import sys

n = int(input())
ans = [0]*n
pm = list()
for i in range(n):
    ans[i] = int(sys.stdin.readline().strip())
plane = deque()
for i in range(n):
    plane.append(i+1)

stack = deque()
flag = 0
for i in range(n):
    if len(stack) == 0:
        pm.append('+')
        stack.append(plane.popleft())
    while(stack[-1] != ans[i]):
        if len(plane) == 0 or stack[-1] > plane[0]:
            flag = 1
            break
        else:
            pm.append('+')
            stack.append(plane.popleft())
    pm.append('-')
    plane.append(stack.pop())
    if flag:
        break
if flag:
    print('NO')
else:
    for i in pm:
        print(i)
