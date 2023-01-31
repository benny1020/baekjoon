"""
1. 이모티콘 플러스 서비스 가입자 최대한 늘리기
2. 이모티콘 판매액을 최대한 늘리는 것

n명의 사용자에개 m개의 이모티콘 할인 판매
할인율은 10 ~ 40 

각 사용자들은 자신의 기준에 따라 일정 비율 이상 할인하는 이모티콘을 모두 구매

"""
from itertools import product
def solution(users, emoticons):
    answer = []

    for i in product([10,20,30,40], repeat = len(emoticons)):
        count = 0
        total = 0
        for user in users:
            userTotal = 0
            for j in range(len(emoticons)):
                if i[j] >= user[0]:
                    userTotal += ((100-i[j])*emoticons[j]/100)
            if userTotal >= user[1]:
                count+=1
            else:
                total += userTotal
                
        
        answer.append([count, total])
    answer = sorted(answer, key = lambda x : (x[0], x[1]), reverse=True)
    return answer[0]
            
