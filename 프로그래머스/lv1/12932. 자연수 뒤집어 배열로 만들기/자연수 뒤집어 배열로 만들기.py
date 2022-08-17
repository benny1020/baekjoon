def solution(n):
    answer = []
    li = list(str(n))
    a = []
    for i in range(len(li)):
        a.append(int(li[len(li)-1-i]))
    return a