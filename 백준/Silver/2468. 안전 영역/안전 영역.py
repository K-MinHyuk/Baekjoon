import sys
from sys import stdin
sys.setrecursionlimit(10000)
def dfs(i, j):
    global m_bool, visited
    if i+1 < len(m_bool) and m_bool[i+1][j] == 1 and not visited[i+1][j]:
        visited[i+1][j] += 1
        dfs(i+1, j)
    if 0 <= i-1 and m_bool[i-1][j] == 1 and not visited[i-1][j]:
        visited[i-1][j] += 1
        dfs(i-1, j)
    if j+1 < len(m_bool[0]) and m_bool[i][j+1] == 1 and not visited[i][j+1]:
        visited[i][j+1] += 1
        dfs(i, j+1)
    if 0 <= j-1 and m_bool[i][j-1] == 1 and not visited[i][j-1]:
        visited[i][j-1] += 1
        dfs(i, j-1)
        
input = stdin.readline
N = int(input())
m = []
max_h = 0
max_cnt = 0
for _ in range(N):
    line = list(map(int, input().strip().split()))
    m.append(line)
    if max_h < max(line):
        max_h = max(line)
        
for h in range(max_h, -1, -1):
    m_bool = [[0 if line_h <= h else 1 for line_h in line] for line in m]
    visited = [[0]*len(m[0]) for _ in range(len(m))]
    cnt = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m_bool[i][j] and not visited[i][j]:
                cnt += 1
                visited[i][j] += 1
                dfs(i, j)
    if max_cnt < cnt:
        max_cnt = cnt
        
print(max_cnt)