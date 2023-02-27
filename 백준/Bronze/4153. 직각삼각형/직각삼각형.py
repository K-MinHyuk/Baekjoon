import sys

while True:
    line = list(map(int, sys.stdin.readline().strip().split()))
    if line[0] == 0 and line[1] == 0 and line[2] == 0:
        break
    t = 0
    for i in range(3):
        if line[i] >= line[t] :
            t = i
    line[2], line[t] = line[t], line[2]
    if line[1]**2 + line[0]**2 == line[2]**2:
        print('right')
    else:
        print('wrong')

        