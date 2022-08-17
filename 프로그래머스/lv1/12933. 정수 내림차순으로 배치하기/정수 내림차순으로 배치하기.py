def solution(n):
    answer = 0
    a=[]
    li = list(str(n))
    for i in range(len(li)):
        a.append(int(li[i]))
    a.sort(reverse=True)
    s=""
    for i in a:
        s+=str(i)
    return int(s)