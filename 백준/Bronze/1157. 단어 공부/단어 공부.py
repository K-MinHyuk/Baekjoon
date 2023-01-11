li = [0]*26
s = input().lower()
for i in s:
    li[ord(i)-ord('a')] += 1

s = max(li)
c = li.index(s)
li.pop(c)
if max(li) == s:
    print('?')
else:
    print(chr(c+ord('A')))
