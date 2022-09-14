from collections import deque

def nextNumber(num, n):
    
    num = deque(num)
    num[-1] += 1
    
    tmp = 0

    for i in reversed(range(len(num))):

        if tmp == 1:
            num[i] += 1
            tmp = 0
            
            if num[i] != n:
                break
            
        if num[i] == n :
            num[i] = 0
            tmp=1
            if i == 0:
                num.appendleft(1)
        

    return list(num)
    
def liToNum(num):
    n = ""
    d = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    for i in num:
        n += d[i]
    return n
    
def solution(n, t, m, p):
    start = [0]
    ans = ""

    for i in range(1,m*t):
        ans += liToNum(start)
        if len(ans)>=t*m:
            break
        start = nextNumber(start,n)
    

    answer=""
    trial = 0
    for i in range(1,len(ans)+1):
        if (i) % m == p or (p == m and i % m ==0 ):
            answer += ans[i-1]
            trial +=1
        if trial == t:
            break
    
        # 0 1 10 11 100 010100
    
    return answer