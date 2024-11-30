import sys; input = sys.stdin.readline;
R = 31
M = 1234567891
def hash(string):
    c = 0
    baseNum = ord("a") - 1
    for i, alpha in enumerate(string):
        c += (ord(alpha) - baseNum)*(R**i)
    return c%M

strLen = int(input())
string = input().rstrip()
print(hash(string))

