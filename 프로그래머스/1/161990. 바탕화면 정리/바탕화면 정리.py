def solution(wallpaper):
    min_x = len(wallpaper[0])
    min_y = len(wallpaper)
    max_x = 0
    max_y = 0
    for y, line in enumerate(wallpaper):
        for x, element in enumerate(line):
            if element == '#':
                if y < min_y:
                    min_y = y
                if x < min_x:
                    min_x = x
                if y+1 > max_y:
                    max_y = y+1
                if x+1 > max_x:
                    max_x = x+1
    answer = [min_y, min_x, max_y, max_x]
    return answer