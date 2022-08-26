'''
성격지표
1번 R T
2번 C F
3번 J M
4번 A N
1 매우 비동의 +3
7 매우 동의 반대 +3

'''

def solution(survey, choices):
    answer = ''
    res = dict()
    res['R'] = 0
    res['C'] = 0
    res['J'] = 0
    res['A'] = 0
    res['T'] = 0
    res['F'] = 0
    res['M'] = 0
    res['N'] = 0
    
    for i in range(len(survey)):
        res[survey[i][0]] += 4 - choices[i]
    
    if res['R'] >= res['T']:
        answer+='R'
    else:
        answer+='T'
        
    if res['C'] >= res['F']:
        answer+='C'
    else:
        answer+='F'
        
    if res['J'] >= res['M']:
        answer+='J'
    else:
        answer+='M'
        
    if res['A'] >= res['N']:
        answer+='A'
    else:
        answer+='N'
        
    
    return answer