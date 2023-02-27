import sys

N = int(input())

temp = list([])
for i in range(N):
    temp.append(list(map(int, sys.stdin.readline().strip().split())))
temp.sort(key=lambda x: (x[0], x[1]))
for i in temp:
    print(*i)