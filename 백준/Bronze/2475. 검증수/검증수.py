l = list(map(int, input().split()))
t = 0
for i in l:
    t += i**2
print(t%10)