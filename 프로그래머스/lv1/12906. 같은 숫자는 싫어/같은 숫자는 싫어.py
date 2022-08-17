def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    tmp = arr[0]
    answer.append(tmp)
    for i in range(1,len(arr)):
        if tmp != arr[i]:
            answer.append(arr[i])
            tmp = arr[i]
        
    
    return answer