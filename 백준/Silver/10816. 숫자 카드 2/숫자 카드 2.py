import sys

N = int(input())
line = list(map(int, sys.stdin.readline().strip().split()))
M = int(input())
key = list(map(int, sys.stdin.readline().strip().split()))
dic = dict.fromkeys(key, 0)
for i in range(N):
    k = line[i]
    if k in dic:
        dic[k] += 1

for i in key:
    print(dic[i], end=' ')