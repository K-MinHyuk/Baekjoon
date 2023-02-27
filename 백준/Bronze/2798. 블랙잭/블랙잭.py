N, MAX = map(int, input().split())
line = list(map(int, input().split()))
book = list()
for i, a in enumerate(line):
    for j, b in enumerate(line[min(i+1, len(line)):]):
        for k, c in enumerate(line[min(j+i+2, len(line)):]):
            book.append(a+b+c)

max_num = 0
for i in book:
    if i > max_num and i <= MAX:
        max_num = i
print(max_num)


