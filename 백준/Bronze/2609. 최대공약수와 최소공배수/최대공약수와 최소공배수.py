def GCD(b, s):
    if b % s == 0:
        return s
    else:
        return GCD(s, b%s)

n, m = map(int, input().split())

if n > m:
    div = GCD(n, m)
    mul = n*m//div
    print(div)
    print(mul)
else:
    div = GCD(m, n)
    mul = n*m//div
    print(div)
    print(mul)