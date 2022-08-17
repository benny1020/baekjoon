def solution(s):
    answer = True
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    li = []
    for i in s:
        if i =='(':
            li.append(1)
        else:
            if len(li) == 0:
                return False
            li.pop()
        
    if len(li) == 0:
        return True
    else:
        return False