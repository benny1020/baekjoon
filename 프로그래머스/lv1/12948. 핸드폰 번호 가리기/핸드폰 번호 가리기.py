def solution(phone_number):
    ans = list(phone_number)
    for i in range(len(phone_number)-4):
        ans[i] = '*'
    s=""
    for  i in range(len(phone_number)):
        s+=ans[i]
    
    
    return s