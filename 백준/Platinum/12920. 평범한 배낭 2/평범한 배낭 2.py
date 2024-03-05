from sys import stdin
input = stdin.readline
N, M = map(int, input().split())
dp = [0 for _ in range(M+1)]
for _ in range(N):
    V, C, K = map(int, input().split())
    p = 1
    while K > 0:
        num = min(K, p)
        for w in range(M, V*num-1, -1):
            dp[w] = max(dp[w], dp[w-V*num]+C*num) 
        p *= 2
        K -= num
print(dp[M])