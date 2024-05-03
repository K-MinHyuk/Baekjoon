from sys import stdin
import sys
sys.setrecursionlimit(10000)
input = stdin.readline
N = int(input())
m = []
count_rg_b = 0
count_r_g_b = 0
for _ in range(N):
    m.append(list(input().strip()))
visited_rg_b = [[0]*len(m[0]) for _ in range(N)]
visited_r_g_b = [[0]*len(m[0]) for _ in range(N)]
def compare(char_in, char_to):
    if char_in == 'B':
        return char_in == char_to
    else:
        return (char_to == 'G') or (char_to == 'R')
    
def dfs_rg_b(i, j):
    global visited_rg_b, m
    if i+1 < len(m) and compare(m[i][j], m[i+1][j]) and not visited_rg_b[i+1][j]:
        visited_rg_b[i+1][j] += 1
        dfs_rg_b(i+1, j)
    if 0 <= i-1 and compare(m[i][j], m[i-1][j]) and not visited_rg_b[i-1][j]:
        visited_rg_b[i-1][j] += 1
        dfs_rg_b(i-1, j)
    if j+1 < len(m) and compare(m[i][j], m[i][j+1]) and not visited_rg_b[i][j+1]:
        visited_rg_b[i][j+1] += 1
        dfs_rg_b(i, j+1)
    if 0 <= j-1 and compare(m[i][j], m[i][j-1]) and not visited_rg_b[i][j-1]:
        visited_rg_b[i][j-1] += 1
        dfs_rg_b(i, j-1)

            
def dfs_r_g_b(i, j):
    global visited_r_g_b, m
    if i+1 < len(m) and m[i][j] == m[i+1][j] and not visited_r_g_b[i+1][j]:
        visited_r_g_b[i+1][j] += 1
        dfs_r_g_b(i+1, j)
    if 0 <= i-1 and m[i][j] == m[i-1][j] and not visited_r_g_b[i-1][j]:
        visited_r_g_b[i-1][j] += 1
        dfs_r_g_b(i-1, j)
    if j+1 < len(m) and m[i][j] == m[i][j+1] and not visited_r_g_b[i][j+1]:
        visited_r_g_b[i][j+1] += 1
        dfs_r_g_b(i, j+1)
    if 0 <= j-1 and m[i][j] == m[i][j-1] and not visited_r_g_b[i][j-1]:
        visited_r_g_b[i][j-1] += 1
        dfs_r_g_b(i, j-1)

        
for i in range(N):
    for j in range(len(m[0])):
        if not visited_rg_b[i][j]:
            visited_rg_b[i][j] += 1
            count_rg_b += 1
            dfs_rg_b(i, j)
            
        if not visited_r_g_b[i][j]:
            visited_r_g_b[i][j] += 1
            count_r_g_b += 1
            dfs_r_g_b(i, j)


    
print(count_r_g_b, count_rg_b)

