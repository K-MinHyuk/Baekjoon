import sys

M = int(input())
for i in range(M):
    H, W, N = map(int, sys.stdin.readline().strip().split())
    d, m = (N%H), (N//H)+1
    if d == 0:
        d = H
        m = (N//H)
    print('{}{:02d}'.format(d,m))

