"""
1 -> 1  1개 
2 -> 1 + 1, 2  2개
3 -> 1 + 1 + 1, 1 + 2, 3   3개
4 -> 1 + 1 + 1 + 1, 2 + 1 + 1, 2 + 2, 1 + 3, 4   5개
5 -> 1 + 1 + 1 + 1 + 1, 2 + 1 + 1 + 1, 3 + 1 + 1, 2 + 2 + 1, 3 + 2, 4 + 1, 5 7개
시발

"""
def solution(n):
    num = 0
    for i in range(1,n+1):
        total = 0
        for j in range(i,n+1):
            total+=j
            if total == n:
                num+=1
                break
            if total > n:
                break
            

    return num