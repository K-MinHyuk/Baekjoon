import sys
input = sys.stdin.readline
h, m, s = map(int, input().split(' '))
cook_time = int(input())
cur_time = h*3600 + m*60 + s
r_time = cook_time + cur_time
r_h = (r_time//3600)%24
r_m = (r_time%3600)//60
r_s = (r_time%3600)%60

print('{} {} {}'.format(r_h, r_m, r_s))