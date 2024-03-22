def floid(N, adj):    
    for i in range(N):
        for s in range(N):
            for d in range(N):
                if adj[s][i] + adj[i][d] < adj[s][d]:
                    adj[s][d] = adj[s][i] + adj[i][d]
    return adj

def solution(N, road, K):
    adj = [[float('inf')]*N for i in range(N)]
    for i in road:
        if adj[i[0]-1][i[1]-1] > i[2]:
            adj[i[0]-1][i[1]-1] = i[2]
            adj[i[1]-1][i[0]-1] = i[2]
    for i in range(N):
        adj[i][i] = 0
    adj = floid(N, adj)
    cnt = 0
    for i in range(N):
        if adj[0][i] <= K:
            cnt += 1  
    print(adj)
    return cnt