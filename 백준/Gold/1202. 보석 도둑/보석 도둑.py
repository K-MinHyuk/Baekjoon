import sys
import heapq

N, K = map(int, sys.stdin.readline().split())
gem = []
bag = []
for i in range(N):
    gem.append(list(map(int, sys.stdin.readline().split()))[::-1])
for i in range(K):
    bag.append(int(sys.stdin.readline()))

gem = sorted(list(gem), key = lambda x: x[1])
bag = sorted(list(bag))
result = 0
pq = []
idx = 0

for size in bag:
    if idx == len(gem):
        if pq:
            result -= heapq.heappop(pq)[0]
    else:
        if size >= gem[idx][1]:
            while idx < len(gem) and size >= gem[idx][1]:
                heapq.heappush(pq, (-gem[idx][0], gem[idx][1]))
                idx += 1
            result -= heapq.heappop(pq)[0]
        elif pq:
            result -= heapq.heappop(pq)[0]
        
print(result)
