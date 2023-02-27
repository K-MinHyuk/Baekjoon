n, m = map(int, input().split())
trun_1 = 1
for i in range(n, n-m, -1):
    trun_1 *= i

trun_2 = 1
for i in range(1, m+1):
    trun_2 *= i

print(trun_1//trun_2)
