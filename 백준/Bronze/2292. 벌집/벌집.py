import sys; input = sys.stdin.readline
num = int(input())
if num == 1:
    print(1)
else:
    a1 = 1
    a2 = 1
    while True:
        if a1 + (a2*6) >= num:
            print(a2+1)
            break
        else:
            a1 = a1 + (a2*6)
            a2 += 1