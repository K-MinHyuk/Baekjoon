# from collections import deque
# def solution(n, computers):
#     q = deque()
#     cluster = [0]*n
#     c = 0
#     for i in range(n):
#         c += 1
#         for j in range(i, n):
#             if computers[i][j] == 1 and cluster[j] == 0:
#                 cluster[j] = c
#                 q.append(j)
#             while q:
#                 d = q.popleft()
#                 for k in range(d, n):
#                     if computers[d][k] == 1 and cluster[k] == 0:
#                         cluster[k] = c
#                         q.append(k)
                        
#     answer = len(set(cluster))
#     return answer


def union(nl, x, y):
    y = find(nl, y)
    x = find(nl, x)
    if x > y:
        nl[x] = y
    else:
        nl[y] = x
        
    
def find(nl, x):
    if nl[x] == x:
        return x
    else:
        return find(nl, nl[x])


def solution(n, computers):
    node_list = [i for i in range(n)]
    for i, line in enumerate(computers):
        for j in range(n):
            if i == j :
                continue
            if line[j] == 1:
                union(node_list, i, j)
    c = set()
    for i in range(n):
        c.add(find(node_list, i))
    return len(c)
