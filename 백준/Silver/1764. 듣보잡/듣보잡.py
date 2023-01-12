import sys

N, M = map(int, input().split())
name = set()
result = list()
for i in range(N):
    name.add(sys.stdin.readline().strip())
for i in range(M):
    s = sys.stdin.readline().strip()
    if s in name:
        result.append(s)
result.sort()
print(len(result))
print(*result, sep='\n')