from sys import stdin
input = stdin.readline
T = int(input())
for _ in range(T):    
    k = int(input())
    n = int(input())
    if n == 1:
        print(1)
        continue
    dp = [i+1 for i in range(n)]
    for i in range(k):
        for j in range(1, n):
            dp[j] += dp[j-1]
    print(dp[-1])
