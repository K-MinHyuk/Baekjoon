import sys
input = sys.stdin.readline
h, m, s = map(int, input().split(' '))

total = int(input())
d_h = total//3600
l_h = total%3600
d_m = l_h//60
d_s = l_h%60

r_s = s + d_s
r_m = m + d_m
r_h = h + d_h

if r_s >= 60:
    r_m += 1
    r_s -= 60
    
if r_m >= 60:
    r_h += 1
    r_m -= 60

print('{} {} {}'.format((r_h)%24, r_m, r_s))