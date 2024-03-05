import sys 

N, K = map(int, sys.stdin.readline().split())
dp = [[0]*(K+1) for i in range(N+1)]
item = [[0,0]]
max_val = -float('inf')

for i in range(N):
    item.append(list(map(int, sys.stdin.readline().split())))

for i in range(N+1):
    for j in range(K+1):
        if j == item[i][0] and dp[i-1][j] < item[i][1]:
            dp[i][j] = item[i][1]
        elif j > item[i][0] and dp[i-1][j] < (dp[i-1][j-item[i][0]] + item[i][1]):
            dp[i][j] = dp[i-1][j-item[i][0]] + item[i][1]
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][K])
