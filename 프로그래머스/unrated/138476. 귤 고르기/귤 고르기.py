"""
k개 골라서 상자 하나에 담아서
귤을 크기별로 분류했을 때 서로 다른 종류의 수를 최소화

제일 종류가 개수가 적은거부터 빼야함
"""
def solution(k, tangerine):
    answer = 0
    tangerine.sort()
    tangerineDict = dict()
    tangerineSet = set(tangerine)
    
    for tanger in tangerineSet:
        tangerineDict[tanger] = 0
    
    for tanger in tangerine:
        tangerineDict[tanger] += 1
    
    # 조합을 확인하자 
    sortedTangerine =  sorted(tangerineDict.items(), key = lambda x : x[1])

    num = []
    k = len(tangerine) - k
    answer = len(set(tangerine))
    for tanger in sortedTangerine:
        if k > tanger[1]:
            num.append(tanger[1])
            k -= tanger[1]
            answer -= 1
        else:
            if k == tanger[1]:
                answer -=1
            num.append(k)
            k = 0
            break
    return answer
    