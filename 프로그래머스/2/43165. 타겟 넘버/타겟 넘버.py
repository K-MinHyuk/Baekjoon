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
import sys
from collections import deque
all_cnt = 0

def solution(numbers, target):
    global ch, all_cnt
    ch = [0]*len(numbers)
    DFS(0, numbers, target)
    return all_cnt

def DFS(v, numbers, target):
    global ch, all_cnt
    if v == len(numbers):
        cnt = 0
        for i in range(len(numbers)):
            if ch[i] == 1:
                cnt += numbers[i]
            else:
                cnt -= numbers[i]
        if cnt == target:
            all_cnt += 1
    else:
        ch[v] = 1
        DFS(v+1, numbers, target)
        ch[v] = 0
        DFS(v+1, numbers, target)
      