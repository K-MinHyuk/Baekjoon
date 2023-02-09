n = int(input())
a, b = divmod(n, 5)

if b == 0:
    print(a)
elif a == 0 and b == 3:
    print(1)
elif a >= 1 and b == 1:
    print(a+1)
elif a>=2 and b == 2:
    print(a+2)
elif b == 3:
    print(a+1)
elif a>=1 and b == 4:
    print(a+2)
else:
    print(-1)