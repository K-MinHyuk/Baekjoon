from collections import deque
def do(dq):
    _ = dq.popleft()
    if len(dq) == 1:
        return dq
    dq.append(dq.popleft())
    return dq

N = int(input())
bin = deque(list(range(1, N+1)))
while len(bin) != 1:
    bin = do(bin)

print(bin[0])