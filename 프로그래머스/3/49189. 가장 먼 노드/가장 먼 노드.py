from collections import deque
def solution(n, edge):
    adj = [[] for _ in range(n)]
    visited = [0]*n
    visited[0] = -1
    q = deque()
    distance = 1
    
    for u, v in edge:
        adj[u-1].append(v-1) 
        adj[v-1].append(u-1)
    
    for i in adj[0]:
        if not visited[i]:
            visited[i] = 1
            q.append(i)
    while q:
        n = q.popleft()
        for i in adj[n]:
            if not visited[i]:
                visited[i] = visited[n] + 1
                q.append(i)
                if visited[i] > distance:
                    distance = visited[i]
                    cnt = 1
                elif visited[i] == distance:
                    cnt += 1
    return cnt
