N = int(input())
for i in range(N):
    n, s = input().split()
    for j in s:
        print(j*int(n), end='')
    print()