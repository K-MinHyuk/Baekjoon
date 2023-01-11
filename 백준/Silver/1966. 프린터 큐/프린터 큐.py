from collections import deque
import sys 

N = int(input())
for i in range(N):
    num, idx = map(int, sys.stdin.readline().strip().split())
    pr = deque(map(int, sys.stdin.readline().strip().split()))
    book = deque(sorted(pr, reverse=True))
    pp = deque(range(num))
    t = 0
    while True:
        pri = pr.popleft()
        if book[0] == pri:
            _ = book.popleft()
            f = pp.popleft()
            t += 1
            if f == idx:
                print(t)
                break
        else:
            pr.append(pri)
            pp.append(pp.popleft())

