N = int(input())
numlist = set(map(int, input().split()))
baselist = list(range(2,1000))

book = set({2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31})

for i in baselist:
    if i % 2 == 0:
        continue
    if i % 3 == 0:
        continue
    if i % 5 == 0:
        continue
    if i % 7 == 0:
        continue
    if i % 11 == 0:
        continue
    if i % 13 == 0:
        continue
    if i % 17 == 0:
        continue
    if i % 19 == 0:
        continue
    if i % 23 == 0:
        continue
    if i % 29 == 0:
        continue
    if i % 31 == 0:
        continue
    book.add(i)
cnt = 0
for i in numlist:
    if i in book:
        cnt += 1
print(cnt) 