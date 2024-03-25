from collections import deque

def solution(maps):
    M = [[int(l) if l != 'X' else l for l in line] for line in maps]
    dx, dy = [1, 0 , -1, 0], [0, 1, 0, -1] 
    check = [[-1]*len(maps[0]) for i in range(len(maps))]
    stage = deque([])
    s = []
    cnt = -1
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if M[i][j] != 'X' and check[i][j] == -1:
                cnt += 1
                check[i][j] = cnt
                s.append(0)
                s[cnt] += M[i][j]
                stage.append((i, j))
                
            while len(stage) > 0:
                I, J = stage.pop()
                for k in range(4):
                    dI, dJ = I+dy[k], J+dx[k]
                    if (0 <= dI < len(maps) and 0 <= dJ < len(maps[0]) and 
                        check[dI][dJ] == -1 and M[dI][dJ] != 'X'):
                        
                        check[dI][dJ] = cnt
                        s[cnt] += M[dI][dJ]
                        stage.append((dI, dJ))
                        
            
    if len(s) == 0:
        return [-1]
    else:
        return sorted(s)
                        