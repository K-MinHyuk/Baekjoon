from sys import stdin
input = stdin.readline
N = int(input())
schedule = []
for i in range(N):
    schedule.append(list(map(int, input().split())))

schedule = sorted(schedule, key=lambda x: (x[1], x[0]))

cnt = 0
last_time = 0
for ss, se in schedule:
    if ss >= last_time:
        cnt += 1
        last_time = se
    
print(cnt)