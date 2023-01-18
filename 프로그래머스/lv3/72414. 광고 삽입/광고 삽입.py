"""
파란색선 -> 동영상 전체 재생구간
검은색 선 -> 죠르디의 동영상을 재생한 구간
빨간색선 -> 최적의 공익광고 위치 -> 누적 재생 시간이 가장 크도록

공익광고가 들어갈 시작 시간

"""
# 시간 문자열을 총 시간으로 변환
def getTime(t):
    h,m,s = map(int,t.split(':'))
    return h*60*60 + m*60 + s

def getTimeStr(t):
    h = t//(60*60)
    t -= h*60*60
    m = t//60
    t -= m*60
    s = t
    
    answer = ""
    if h < 10:
        answer+='0'
    answer+=str(h)
    answer+=':'
    
    if m < 10:
        answer+='0'
    answer+=str(m)
    answer+=':'
    if s < 10:
        answer+='0'
    answer+=str(s)

    return answer
    
def solution(play_time, adv_time, logs):
    times = []
    dp = [0 for i in range(getTime(play_time)+1)]
    for log in logs:
        t = log.split('-')
        times.append([getTime(t[0]), getTime(t[1])])


    for time in times:

        dp[time[0]]+=1
        dp[time[1]]-=1

        
    for i in range(1,len(dp)):
        dp[i] += dp[i-1]
    
    s = 0
    for i in range(getTime(adv_time)):
        s += dp[i]

    maxTime = s
    maxStart = 0
    
    #return getTime("01:30:59")
    
    for j in range(getTime(play_time)-getTime(adv_time)+1):
        s += dp[j+getTime(adv_time)]
        s -= dp[j]

        if maxTime < s:
            maxTime = s
            maxStart = j+1
    return getTimeStr(maxStart)
    # getTime(adv_time) +1 ~ 마지막까지



