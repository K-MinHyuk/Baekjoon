from sys import stdin
from collections import deque
input = stdin.readline
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
t = int(input())

for i in range(t):
    M, N, K = map(int, input().split())
    mp = [[0]*M for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    yx = []
    q = deque()
    count = 0
    for _ in range(K):
        x, y = map(int, input().split())
        yx.append([y, x])
        mp[y][x] = 1
    for item in yx:
        if not visited[item[0]][item[1]]:
            count += 1
            q.append(item)
            while q:
                y, x = q.pop()
                if visited[y][x] :
                    continue
                else:
                    visited[y][x] = 1
                    for i in range(4):
                        Dx, Dy = x+dx[i], y+dy[i]
                        if 0 <= Dx < M and 0 <= Dy < N and mp[Dy][Dx] and not visited[Dy][Dx]:
                            q.append([Dy, Dx])
    print(count)