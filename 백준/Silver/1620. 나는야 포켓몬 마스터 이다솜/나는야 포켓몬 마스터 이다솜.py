import sys

n, m = map(int, input().split())
name = dict()
num = dict()

for i in range(1, n+1):
    word = sys.stdin.readline().strip()
    name[str(i)] = word
    num[word] = i

for i in range(m):
    word = sys.stdin.readline().strip()
    if word in name:
        print(name[word])
    else:
        print(num[word])
