import sys
from sys import stdin
input = stdin.readline
N = int(input())
A = list(map(int, input().split()))
dp = [1]*N
for i in range(N):
    for j in range(i-1, -1, -1):
        if A[i] > A[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
print(max(dp))    