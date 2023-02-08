import sys
import collections

line = sys.stdin.readline().strip()
stack = collections.deque()
buff = ''
stick = 0

for i in line:
    if len(stack) == 0:
        stack.append(i)
        buff = i
    else:
        if i == '(':
            stack.append(i)
            buff = i
        elif i == ')' and buff != i:
            stack.pop()
            stick += len(stack)
            buff = i

        elif i == ')' and buff == i:
            stack.pop()
            stick += 1
            buff = i

print(stick)
