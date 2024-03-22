def solution(sizes):
    maximumx = -1
    maximumy = -1
    s = [sorted(i) for i in sizes]
    for i in s:
        if i[0] >= maximumx:
            maximumx = i[0]
        if i[1] >= maximumy:
            maximumy = i[1]
    return maximumx*maximumy