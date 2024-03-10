from sys import stdin
input = stdin.readline
N = int(input())
schedule = []
for i in range(N):
    schedule.append(list(map(int, input().split())))

schedule = sorted(schedule, key=lambda x: (x[0], x[1]))

cnt = 1
last_time = [0]
for ss, se in schedule:
    for i in range(len(last_time)):
        if ss >= last_time[i]:
            last_time[i] = se
            break
    else:
        last_time.append(se)
        cnt += 1
    
print(cnt)