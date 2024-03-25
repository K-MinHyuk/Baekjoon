def conf(time):
    hh, mm = map(int, time.split(':'))
    hh *= 60
    return hh + mm

def solution(book_time):
    room = [[0]*1441]    
    table = []
    room_max = 1
    
    for book in book_time:
        table.append(list(map(conf, book)))
    table = sorted(table, key= lambda x : (x[0], x[1]))
    
    for bs, be in table:
        for i in range(room_max):
            if sum(room[i][bs:be+10]) == 0:
                room[i][bs:be+10] = [1]*len(room[i][bs:be+10])
                break
        else:
            temp = [0]*1441
            temp[bs:be+10] = [1]*len(temp[bs:be+10])
            room.append(temp)
            room_max += 1
                
    return room_max