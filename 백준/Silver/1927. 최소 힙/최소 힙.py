from queue import PriorityQueue
import sys
N = int(sys.stdin.readline().strip())
pq = PriorityQueue()
for i in range(N):
    num = int(sys.stdin.readline().strip())
    if num == 0:
        if pq.qsize() == 0:
            print(0)
        else:
            print(pq.get())
    else:
        pq.put(num)

