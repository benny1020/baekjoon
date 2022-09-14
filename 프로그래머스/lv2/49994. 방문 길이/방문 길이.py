# L L D D U D
def solution(dirs):
    check = [[[0 for i in range(4)] for j in range(12)] for k in range(12)]
    
    cur = [0,0]
    
    ans = 0
    
    # -5 -> 0
    # 5 -> 10 
    # 범위 체크
    # visit check
    # visit 처리 후 넘김
    for d in dirs:
        if d == 'U':
            if cur[1] + 1 == 6:
                continue
            
            if check[cur[0]+5][cur[1]+5][0] == False:
                ans += 1
                check[cur[0]+5][cur[1]+5][0] = True # U visit처리
                check[cur[0]+5][cur[1]+6][1] = True # 한칸 위에서 D visit 처리
                
            cur[1] += 1

            
        elif d == 'D':
            if cur[1] - 1 == -6:
                continue
            
            if check[cur[0]+5][cur[1]+5][1] == False:
                ans += 1
                
                check[cur[0]+5][cur[1]+5][1] = True # U visit처리
                check[cur[0]+5][cur[1]+4][0] = True # 한칸 아래에서 U visit 처리
                
            cur[1] -= 1
        
        elif d == 'L':
            if cur[0] - 1 == -6:
                continue
            
            if check[cur[0]+5][cur[1]+5][2] == False:
                ans += 1
                check[cur[0]+5][cur[1]+5][2] = True # L visit처리
                check[cur[0]+4][cur[1]+5][3] = True # 한칸 왼쪽에서에서 R visit 처리
                
            cur[0] -= 1 
        
        elif d == 'R':
            if cur[0] + 1 == 6:
                continue
            
            if check[cur[0]+5][cur[1]+5][3] == False:
                ans += 1
                check[cur[0]+5][cur[1]+5][3] = True # R visit처리
                check[cur[0]+6][cur[1]+5][2] = True # 한칸 왼쪽에서에서 L visit 처리
                
            cur[0] += 1
        

    return ans