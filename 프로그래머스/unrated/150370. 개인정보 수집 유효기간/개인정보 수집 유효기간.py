"""
1~n 개인정보
1월 5일부터 1년이면 1월 4일

파기해야할 번호 반환
"""

def dayToTimestamp(today):
    year, month, day = map(int, today.split('.'))
    return 336*year + (month-1)*28 + day
 
def solution(today, terms, privacies):
    answer = []
    
    todayDays = dayToTimestamp(today)
    
    termDict = dict()

    for term in terms:
        kind = term.split(' ')[0]
        month = int(term.split(' ')[1])
        termDict[kind] = month
    
    cur = 1

    for privacy in privacies:
        days = dayToTimestamp(privacy.split(' ')[0])
        kind = privacy.split(' ')[1]
        print(todayDays-days, termDict[kind])
        if todayDays - days >= termDict[kind]*28:
        
            answer.append(cur)
        cur += 1
    return answer
        


    

