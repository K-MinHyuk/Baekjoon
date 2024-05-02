def find(index):
    global p
    if p[index] != index:
        return find(p[index])
    return index

def union(x, y):
    global p
    x = find(x)
    y = find(y)
    if x < y :
        p[y] = x
    else:
        p[x] = y

def solution(n, costs):
    global p
    costs = sorted(costs, key=lambda x: x[2])
    p = [i for i in range(n)]
    cost = 0
    for edge in costs:
        if find(edge[0]) == find(edge[1]):
            continue
        else:
            union(edge[0], edge[1])
            cost += edge[2]
    return cost