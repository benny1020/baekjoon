import math
def solution(n, words):
    w = [words[0]]
    ans = 0
    for i in range(1,len(words)):
        # 탈락 조건
        # 일치하지 않는 경우
        if words[i][0] != words[i-1][-1]:
            ans = i
            break
            
        if words[i] in w:
            ans = i
            break
        
        # 단어 추가
        w.append(words[i])
        
        #탈락자 없는경우 
        if i == len(words)-1:
            return [0,0]
        
    if ans % n == 0:
        return [ans%n+1,ans/n+1]
    else:
        return [ans%n+1,math.ceil(ans/n)]
    
