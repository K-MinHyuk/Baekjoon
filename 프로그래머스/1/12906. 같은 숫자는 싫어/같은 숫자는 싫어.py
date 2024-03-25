def solution(arr):
    li = [arr[0]]
    for i in range(1,len(arr)):
        if arr[i-1] == arr[i]:
            pass
        else:
            li.append(arr[i])
    answer = li
    
    print('Hello Python')
    return answer