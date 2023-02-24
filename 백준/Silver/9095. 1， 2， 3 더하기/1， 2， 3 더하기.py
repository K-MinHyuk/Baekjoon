import sys
def p(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    return p(n-1) + p(n-2) + p(n-3)


N = int(input())
for i in range(N):
    num = int(sys.stdin.readline().strip())
    print(p(num))