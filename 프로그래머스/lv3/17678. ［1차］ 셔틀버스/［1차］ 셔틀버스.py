"""
셔틀은 9시부터
도착한 순간에 대기열에 선 크루까지 포함해서 순서대로
9시에 도착하면 9시에 줄선 크루도 
운행횟수 n 회
운행간격 t
한번에 탈 수 있는 m 명
콘이 무사히 셔틀타고 사무실로 갈 수 있는 제일 늦은 도착시간
"""
def solution(n, t, m, timetable):
    crew = []
    for time in timetable:
        hour, minute = map(int,time.split(':'))
        crew.append(hour*60 + minute)
    crew.sort()
    """
    마지막 타임만 체크하자
    마지막
    """
    cur = 540
    for i in range(n):
        cnt = 0
        l = len(crew)
        last = 0
        for j in range(l):
            if crew[0] <= cur and cnt < m:
                tmp = crew.pop(0)
                cnt += 1
                if cnt == m:
                    last = tmp
        if i == n-1:
            if last != 0:
                ans = last-1
                print(ans)
            else:
                ans = cur
        cur+=t
    
    hour = str(ans // 60)
    minute = str(ans - (ans//60)*60)
    if len(hour) == 1:
        hour = '0' + hour
    if len(minute) == 1:
        minute = '0' + minute
    return hour+":"+minute
                
                
    
    