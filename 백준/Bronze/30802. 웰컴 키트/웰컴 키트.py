import sys; input = sys.stdin.readline
numPeople = int(input())
sizeList = list(map(int, input().split()))
T, P = map(int, input().split())

minPack = 0
for s in sizeList:
    if s % T == 0 :
        minPack += s//T
    else:
        minPack += s//T + 1
print(minPack)
print(numPeople//P, numPeople%P)
        
        