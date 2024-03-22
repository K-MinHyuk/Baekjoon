def search(t, times):
    people = list()
    for em in times:
        people.append(t//em)
    return sum(people)

def solution(n, times):
    time = min(times)*n
    base = 1
    limit = time
    c_time = time//2
    re = 0
    while base+1 != limit:
        re = search(c_time, times)
        if re >= n:
            limit = c_time
            c_time = (c_time + base)//2  
        else:
            base = c_time
            c_time = (c_time + limit)//2
    print(base, limit)
    if  search(base, times) == n:
        return base
    else:
        return base+1
