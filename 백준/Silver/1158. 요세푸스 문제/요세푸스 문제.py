from collections import deque

def do(dq, K):
    for i in range(K-1):
        dq.append(dq.popleft())
    val = dq.popleft()
    return dq, val


N, K = (map(int, input().split()))

bin = deque(range(1, N+1))
result = deque()

while len(bin) != 0:
    bin, val = do(bin, K)
    result.append(val)

print("<", end='')
print(*result, sep=', ', end='')
print(">")