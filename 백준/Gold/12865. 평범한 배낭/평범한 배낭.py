import sys 

N, K = map(int, sys.stdin.readline().split())
dp = [0]*(K+1)
item = []
max_val = -float('inf')

for i in range(N):
    i_w, i_v = map(int, sys.stdin.readline().split())
    for w in range(K, i_w-1, -1):
        dp[w] = max(dp[w], dp[w-i_w] + i_v)

print(dp[K])
