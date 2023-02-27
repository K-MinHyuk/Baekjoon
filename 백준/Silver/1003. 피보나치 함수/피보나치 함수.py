import sys

N = int(input())
book = {0: [1, 0], 1:[0, 1]}
for i in range(N):
    num = int(sys.stdin.readline().strip())
    if num in book:
        print(*book[num])
    else:
        for j in range(num+1):
            if j in book:
                continue
            else:
                f1 = book[j-1]
                f2 = book[j-2]
                book[j] = [f1[0] + f2[0], f1[1] + f2[1]]
        print(*book[num])
