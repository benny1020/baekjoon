def solution(s):
    
    
    li = [int(x) for x in s.split(' ')]
    return str(min(li)) + ' ' + str(max(li))

    return li
    minous = False
    num = ""
    maxx = None
    minn = None
    for i in range(len(s)):
        if s[i] == ' ' or i == len(s)-1:
            if minous == True:
                num = int(num) * (-1)
            else:
                num = int(num)
            if maxx != None:
                maxx = max(num,maxx)
            else:
                maxx = num
            if minn != None:
                minn = min(num,minn)
            else:
                minn = num
                
            num = ""
            minous = False
            
        elif s[i] == '-':
            minous = True
        else:
            num += s[i]
            
    return str(minn)+' '+str(maxx)
        
        
    return answer