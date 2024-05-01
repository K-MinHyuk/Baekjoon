from sys import stdin
from collections import deque
input = stdin.readline
N, M, V = map(int, input().split())
visited = [0]*N
visited[V-1] = 1
edge = []
for i in range(M):
    f, t = map(int, input().split())    
    edge.append([f, t])
    edge.append([t, f])
edge = sorted(edge, key=lambda x:(x[0], x[1]))
def dfs(start):
    print(start, end=' ')
    for f, t in edge:
        if f == start and not visited[t-1] and visited[f-1]:
            visited[t-1] = 1
            dfs(t)
            
dfs(V)
print()

visited = [0]*N
visited[V-1] = 1

q = deque([V])
while q:
    n = q.popleft()
    print(n, end=' ')
    for f, t in edge:
        if f == n and not visited[t-1] and visited[f-1]:
            visited[t-1] = 1
            q.append(t)
