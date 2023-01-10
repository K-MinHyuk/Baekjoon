import sys

n = int(input())
line = set(map(int, sys.stdin.readline().strip().split()))
m = int(input())
nline = list(map(int, sys.stdin.readline().strip().split()))

for i in nline:
    print(int(i in line))

