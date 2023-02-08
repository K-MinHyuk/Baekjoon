import sys
import collections 
line1 = collections.deque(sys.stdin.readline().strip())
line2 = collections.deque()

n = int(input())

for i in range(n):
    word = sys.stdin.readline().strip().split()
    if word[0] == 'L':
        if len(line1) > 0:
            line2.appendleft(line1.pop())
    elif word[0] == 'P':
        line1.append(word[1])
    elif word[0] == 'B':
        if len(line1) > 0:
            line1.pop()
    elif word[0] == 'D':
        if len(line2) > 0:
            line1.append(line2.popleft())

for i in line1:
    print(i, end='')
for i in line2:
    print(i, end='')