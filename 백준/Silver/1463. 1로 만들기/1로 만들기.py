N = int(input())

bag = [0 for i in range(N+1)]

for i in range(2, N+1):
    bag[i] = bag[i-1]+1
    if i % 3 == 0:
        bag[i] = min(bag[i//3]+1, bag[i])
    if i % 2 == 0:
        bag[i] = min(bag[i//2]+1, bag[i])
    
print(bag[N])