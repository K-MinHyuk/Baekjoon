import sys; input = sys.stdin.readline
N = int(input())
q = [0 for i in range(10000)]
for n in range(N):
    idx = int(input())-1
    q[idx] += 1 
for i in range(10000):
    if q[i] > 0:
        for j in range(q[i]):
            print(i+1)