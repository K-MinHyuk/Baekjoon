from collections import deque
def solution(maps):
    visit = [[0]*len(maps[0]) for _ in range(len(maps))]
    c = 1
    q = deque([[0, 0, c]])
    visit[0][0] = c
    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]
    while q:
        sy, sx, c = q.popleft()
        for i in range(4):
            y = sy + dy[i]
            x = sx + dx[i]
            if 0 <= y < len(maps) and 0 <= x < len(maps[0]) and maps[y][x] == 1 and visit[y][x] == 0:
                visit[y][x] = c+1
                q.append([y, x, c+1])
    if visit[-1][-1] == 0:
        return -1
    else:
        return visit[-1][-1]
