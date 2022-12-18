def getDigit(cnt):
    return len(str(cnt))

def solution(s):
    # 몇개 단위로 짜를까?

    minCount = len(s)

    for i in range(1,len(s)+1//2+1):
        wordCount = dict()
        word = set()
        tmp = s[0:i]

        cnt = 0
        cur = 0
        for j in range(1, len(s)//i):
            if s[i*j:i*(j+1)] == tmp:
                cnt += 1
            else:
                if cnt == 0:
                    cur += len(tmp)
                if cnt > 0:
                    cur += (len(tmp) + getDigit(cnt+1))
                    cnt = 0
                
                tmp = s[i*j:i*(j+1)]
                
        if cnt == 0:
            cur += len(tmp)
        if cnt > 0:
            cur += (len(tmp) + getDigit(cnt+1))
            cnt = 0
            
        cur += (len(s)%i)
        #print(cur)
        minCount = min(minCount, cur)
        
        
        
    return minCount
    
