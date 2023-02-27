import sys

N = int(input())

book = set()
for i in range(N):
    book.add(sys.stdin.readline().strip())

book = list(book)
book.sort(key=lambda x: (len(x), x))
for i in range(len(book)):
    print(book[i])
