from sys import stdin
from collections import deque
input = stdin.readline
N = int(input())
e = int(input())
adj = [[0]*N for i in range(N)]
visited = [0]*N
cnt = 0
for i in range(e):
    s, t = map(int, input().split())
    adj[s-1][t-1] = adj[t-1][s-1] = 1

def dfs(start):
    global cnt
    visited[start] = 1
    for i in range(N):
        if not visited[i] and adj[start][i]:
            cnt += 1
            dfs(i)
dfs(0)
print(cnt)