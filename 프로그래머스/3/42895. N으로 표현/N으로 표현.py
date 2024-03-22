def solution(N, number):
    dp = [0]
    for i in range(1, 9):
        n_number = set()
        n_number.add(int(str(N)*i))
        
        for j in range(1, i):
            for k in dp[j]:
                for l in dp[i-j]:
                    n_number.add(k+l)
                    n_number.add(k*l)
                    n_number.add(k-l)
                    if l != 0:
                        n_number.add(k//l)
        if number in n_number:
            return i
        else:
            dp.append(n_number)
    return -1