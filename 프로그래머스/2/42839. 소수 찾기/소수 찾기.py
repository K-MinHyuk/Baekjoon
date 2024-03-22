from itertools import permutations
def prime_num(num):
    table = [1]*(num+1)
    table[0] = 0
    table[1] = 0
    for i in range(2, int(num**(1/2))+1):
        if table[i] == 1:
            for j in range(i+i, num+1, i):
                if table[j] == 1:
                    table[j] = 0
    return table

def solution(numbers):
    n = set()
    maximum = 0
    cnt = 0
    for i in range(1, len(numbers)+1):
        for k in permutations(numbers, i):
            line = ''
            for i in k:
                line += str(i)
            n.add(int(line))
            if int(line) > maximum:
                maximum = int(line)
    table = prime_num(maximum)   
    
    for item in n:
        if table[item] == 1:
            cnt += 1
    return cnt