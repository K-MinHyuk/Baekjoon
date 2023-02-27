import sys

N = int(input())
name = list([])
for i in range(N):
    name.append(list(sys.stdin.readline().strip().split()))
name.sort(key=lambda x: int(x[0]))

for i in name:
    print(*i)