def solution(num):
    trial = 0
    if num == 1:
        return 0
    while(True):
        if num%2 == 0:
            num /= 2
        else:
            num *=3
            num +=1
        trial+=1
        if num == 1:
            return trial
        if trial>=501:
            return -1
    return answer