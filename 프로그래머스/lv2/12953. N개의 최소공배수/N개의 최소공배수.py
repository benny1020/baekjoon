def solution(arr):
    maxx = max(arr)

    flag = False
    n = 1
    num = maxx
    if len(arr) == 1:
        return max
    while(flag == False):
        for i in range(len(arr)):
            if num % arr[i] != 0:
                break
            if i == len(arr)-1:
                return num
        n+=1
        num = maxx * n
        
            
    return num