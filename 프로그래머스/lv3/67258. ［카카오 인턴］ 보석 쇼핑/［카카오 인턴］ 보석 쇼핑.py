def solution(gems):

    nowGemCount = dict()
    answer = [1,len(gems)]
    for gem in set(gems):
        nowGemCount[gem] = 0
    
    start = 0
    end = 1
    
    nowGemCount[gems[start]]=1

    totalCount = len(set(gems))
    nowCount = 1
    if totalCount == 1:
        answer = [1,1]
    while(end < len(gems) or nowGemCount[gems[start]]>=2):
                
        if nowGemCount[gems[start]] >= 2:
            nowGemCount[gems[start]] -= 1
            if nowGemCount[gems[start]] == 0:
                nowCount -= 1
            start += 1
        else:
            nowGemCount[gems[end]] += 1
            if nowGemCount[gems[end]] == 1:
                nowCount += 1
            end += 1
        if nowCount == totalCount:
            if answer[1] - answer[0] > end - 1 - start :
                answer[0] = start+1
                answer[1] = end
        
            
    return answer
            
            