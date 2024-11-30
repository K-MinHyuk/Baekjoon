import sys; input = sys.stdin.readline
A, B, V = map(int, input().split())
T, remain = divmod(V-A, (A-B))
if remain > 0 :
    print(T+2)
elif remain == 0:
    print(T+1)
else:
    print(T)