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
bag = sorted(list(bag), )
result = 0
pq = []
count = 0

for i in range(len(gem)):
    if gem[i][1] <= bag[count]:
        heapq.heappush(pq, (-gem[i][0], gem[i][1]))
    else:
        while count < len(bag) and len(pq) > 0 and gem[i][1] > bag[count]:
            result -= heapq.heappop(pq)[0]
            count+=1
        while  count < len(bag) and len(pq) == 0 and gem[i][1] > bag[count]:
            count+=1
        if count < len(bag) and gem[i][1] <= bag[count]:
            heapq.heappush(pq, (-gem[i][0], gem[i][1]))
                    
    if count >= len(bag):
        break
else:
    while count < len(bag) and len(pq) > 0:
        result -= heapq.heappop(pq)[0]
        count += 1
print(result)
