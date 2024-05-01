from sys import stdin
from collections import deque
input = stdin.readline
def dfs(i, j):
    global MAP, visited, answer
    visited[i][j] = 1
    answer[-1] += 1
    if 0 <= i+1 < len(MAP) and MAP[i+1][j] == 1 and not visited[i+1][j]:
        dfs(i+1, j)
    if 0 <= i-1 < len(MAP) and MAP[i-1][j] == 1 and not visited[i-1][j]:
        dfs(i-1, j)
    if 0 <= j-1 < len(MAP) and MAP[i][j-1] == 1 and not visited[i][j-1]:
        dfs(i, j-1)
    if 0 <= j+1 < len(MAP) and MAP[i][j+1] == 1 and not visited[i][j+1]:
        dfs(i, j+1)
                
    
N = int(input())
MAP = []
answer = []
for i in range(N):
    MAP.append(list(map(int, list(input().strip()))))
visited = [[0]*len(MAP[0]) for _ in range(len(MAP))]
for i in range(len(MAP)):
    for j in range(len(MAP[0])):
        if MAP[i][j] == 1 and not visited[i][j]:
            answer.append(0)
            dfs(i, j)
answer.sort()
print(len(answer))
for i in answer:
    print(i)