from sys import stdin
from collections import deque
input = stdin.readline
N, M = map(int, input().split())
adj = [[0]*N for _ in range(N)]
visited = [0]*N
count = 0

def dfs(index):
    global visited
    for i in range(N):
        if adj[index][i] and not visited[i]:
            visited[i] = 1
            dfs(i)
    
for i in range(M):
    u, v = map(int, input().split())
    adj[u-1][v-1] = adj[v-1][u-1] = 1
 
for i in range(N):
    if not visited[i]:
        count += 1
        dfs(i)   
print(count)
