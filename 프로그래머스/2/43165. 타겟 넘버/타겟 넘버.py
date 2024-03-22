# from collections import deque
# def solution(numbers, target):
#     q = deque()
#     qq = deque()
#     numbers = sorted(numbers, reverse=True)
#     for i, j in enumerate(numbers):
#         if i == 0:
#             if j - sum(numbers[1:]) <= target:
#                 q.append(j)
#             if -j + sum(numbers[1:]) >= target:
#                 q.append(-j)
#         else:
#             while q:
#                 t = q.popleft()
#                 if t - sum(numbers[i:]) <= target:
#                     qq.append(t - j)
#                 if t + sum(numbers[i:]) >= target:
#                     qq.append(t + j)
#             q = qq
#             qq = deque()
#     cnt = 0
#     for i in range(len(q)):
#         if q[i] == target:
#             cnt+=1
#     answer = cnt
#     return answer
from collections import deque
def solution(numbers, target):
    q = deque()
    qq = deque()
    N = len(numbers)
    numbers = sorted(numbers)
    n = numbers.pop()
    if n - sum(numbers) <= target:
        q.append(n)
    if -n + sum(numbers) >= target:
        q.append(-n)
    for n in numbers[::-1]:
        while q:
            const = q.pop()
            if const + n - sum(numbers) <= target:
                qq.append(const + n)
            if const - n + sum(numbers) >= target:
                qq.append(const - n)
        q = qq
        qq = deque()
    cnt = 0
    for i in q:
        if i == target:
            cnt += 1
    return cnt