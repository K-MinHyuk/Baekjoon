def solution(answers):
    a = [1, 2, 3, 4, 5]*((len(answers)//5) + 1)
    b = [2, 1, 2, 3, 2, 4, 2, 5]*((len(answers)//8)+1)
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*((len(answers)//10)+1)
    cnt = [[0, 1], [0, 2], [0, 3]]
    for i, A in enumerate(answers):
        if a[i] == A:
            cnt[0][0] += 1
        if b[i] == A :
            cnt[1][0] += 1
        if c[i] == A :
            cnt[2][0] += 1
    cnt = sorted(cnt, reverse=True, key=lambda x: x[0])
    if cnt[0][0] == cnt[1][0]:
        if cnt[1][0] == cnt[2][0]:
            return [1, 2, 3]
        return sorted([cnt[0][1], cnt[1][1]])
    else:
        return [cnt[0][1]]