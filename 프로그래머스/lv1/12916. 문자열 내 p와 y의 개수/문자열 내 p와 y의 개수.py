def solution(s):
    answer = True
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    p=0
    y=0
    for i in s:
        if i == 'p' or i == 'P':
            p+=1
        if i == 'y' or i == 'Y':
            y+=1
    if p==y:
        return True
    else:
        return False
    

    return True