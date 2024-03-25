def solution(friends, gifts):
    num_friends = len(friends)
    histo = [[0]*num_friends for _ in range(num_friends)]
    next_gift = [[0]*num_friends for _ in range(num_friends)]
    for cntrct in gifts:
        frm, to = cntrct.split(' ')
        histo[friends.index(to)][friends.index(frm)] += 1
    
    for i in range(num_friends):
        for j in range(i+1, num_friends):
            if i == j:
                continue
            if histo[i][j] > histo[j][i]:
                next_gift[j][i] += 1
            elif histo[i][j] < histo[j][i]:
                next_gift[i][j] += 1
            else:
                giftind1 = sum([histo[k][i] for k in range(num_friends)]) - sum(histo[i])
                giftind2 = sum([histo[k][j] for k in range(num_friends)]) - sum(histo[j])
                
                if giftind1 > giftind2:
                    next_gift[i][j] += 1
                elif giftind2 > giftind1:
                    next_gift[j][i] += 1
                else:
                    continue
                    
        
    answer = max([sum(next_gift[i]) for i in range(num_friends)])
    return answer