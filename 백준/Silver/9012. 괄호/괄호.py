from collections import deque

n = int(input())
for i in range(n):
    line = deque(input())
    if len(line) % 2 == 1:
        print('NO')
        continue
    stack = deque()
    while len(line) != 0:
        if len(stack) == 0:
            stack.append(line.popleft())
        inv = line.popleft()
        ink = stack.pop()
        if not(inv == ')' and ink == '('):
            stack.append(ink)
            stack.append(inv)
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')