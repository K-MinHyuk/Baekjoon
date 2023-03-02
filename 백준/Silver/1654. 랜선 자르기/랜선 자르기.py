import sys
from collections import deque

K, N = map(int, input().split())
line = deque()
high = -float('inf')
low = 1
for i in range(K):
    num = int(sys.stdin.readline().strip())
    line.append(num)
    if num > high:
        high = num

result = 0
while low <= high:
    mid = (high+low)//2
    tm = 0
    for i in line:
        tm+= i//mid
    if tm >= N:
        low = mid + 1
        if result < mid:
            result = mid
    elif tm < N:
        high = mid - 1

print(result)