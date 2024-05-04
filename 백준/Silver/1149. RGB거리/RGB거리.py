from sys import stdin
input = stdin.readline
N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]
dp = [[0, 0, 0] for _ in range(N)] # RGB
dp[0][0] = cost[0][0] 
dp[0][1] = cost[0][1] 
dp[0][2] = cost[0][2]
for i in range(1, N):
    for j in range(3):
     dp[i][j] = min(dp[i-1][(j+1)%3] + cost[i][j], dp[i-1][(j+2)%3] + cost[i][j])
print(min(dp[-1]))