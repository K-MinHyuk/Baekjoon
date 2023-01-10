import sys
from collections import deque

stack = deque()
n = int(input())
for i in range(n):
    num = int(sys.stdin.readline().strip())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)
toc = 0
for i in stack:
    toc += i
print(toc)
