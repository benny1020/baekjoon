def solution(n, m):
    answer = []
    
    # 최대공약수 구하기
    maxx = 1
    for i in range(1,min(n,m)+1):
        if n%i==0 and m%i == 0:
            if maxx < i:
                maxx = i
    minn=99999999
    # 최소공배수 구하기
    if maxx==1:
        minn = m*n
    else:
        for i in range(1,n*m):
            
            if i%n==0 and i%m == 0:
                if minn > i:
                    minn = i
    answer.append(maxx)
    answer.append(minn)
    return answer