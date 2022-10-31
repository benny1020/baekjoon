def solution(sticker):
    n = len(sticker)
    if len(sticker) == 1 or len(sticker) == 2:
        return max(sticker)
    dp = [0 for i in range(n)]
    
    # 첫번째 꺼 선택하고 마지막은 선택 X
    dp[0] = sticker[0]
    dp[1] = sticker[0]
    for i in range(2,n-1):
        dp[i] = max(dp[i-2] + sticker[i], dp[i-1])
    tmp1 = dp[n-2]
    
    # 첫번째꺼 버리고 마지막 선택
    dp[0] = 0
    dp[1] = sticker[1]
    for i in range(2,n):
        dp[i] = max(dp[i-2] + sticker[i], dp[i-1])
    return max(tmp1,dp[n-1])
    
    # 마지막
    
def solution2(sticker):
    if len(sticker) == 1 or len(sticker) == 2:
        return max(sticker)
    
    # 첫번째꺼 선택, 마지막꺼 선택 X
    s1 = sticker[2:len(sticker)-1]

    total = sticker[0]
    
    
    
    # 첫번째꺼 선택 X, 마지막꺼 선택 O
    
    dp_first_select = [[0,0] for i in range(len(sticker))]
    dp_last_select = [[0,0] for i in range(len(sticker))]
    
    # 첫번째꺼 선택하는 경우
    dp_first_select[0][0] = sticker[0]
    dp_first_select[0][1] = sticker[0]    
    
    dp_first_select[1][0] = sticker[0]
    dp_first_select[1][1] = sticker[0]

    for i in range(2, len(sticker)-1):
        dp_first_select[i][0] = max(dp_first_select[i-1])
        dp_first_select[i][1] = max(dp_first_select[i-1][0] + sticker[i], max(dp_first_select[i-2]) + sticker[i])

    dp_first_select[len(sticker)-1][0] = max(dp_first_select[len(sticker)-1])
    
    print(dp_first_select)
    # 마지막꺼 선택하는 경우 첫번째꺼 선택 X
    dp_last_select[0][0] = 0
    dp_last_select[0][1] = 0
    
    dp_last_select[1][0] = 0
    dp_last_select[1][1] = sticker[1]
    
    for i in range(2, len(sticker)):
        dp_last_select[i][0] = max(dp_last_select[i-1])
        dp_last_select[i][1] = max(dp_last_select[i-1][0] + sticker[i], max(dp_last_select[i-2]) + sticker[i])
    
    return max(max(dp_last_select[len(sticker)-1], dp_first_select[len(sticker)-1]))
    
    
"""
global total
total = 0
import sys
sys.setrecursionlimit(110000)
def search(cur, sticker, flag, first_flag, total_number):
    global total
    if cur == 0:
        search(cur+1, sticker, True, True, sticker[cur])
        search(cur+1, sticker, False, False, 0)
        return

    # 종료 조건
    if cur == len(sticker):
        if total < total_number:
            total = total_number
        return
    
    if cur == len(sticker)-1:
        if not flag and not first_flag:
            search(cur+1, sticker, True, first_flag, total_number + sticker[cur])
        else:
            search(cur+1, sticker, False, first_flag, total_number)
        return
    else:
        if flag:
            search(cur+1,sticker, False, first_flag, total_number)
        else:
            search(cur+1, sticker, True, first_flag, total_number + sticker[cur])
        
        return
    return
def solution(sticker):
    global total
    answer = 0
    search(0, sticker, False, False, 0)
    return total
    

    return answer
"""