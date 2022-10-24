def solution(triangle):
    que = [[0, 0, 0]] # 층, cur, sum
    max_sum = 0
    
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == len(triangle[i])-1:
                triangle[i][j] += triangle[i-1][j-1]
            elif j == 0:
                triangle[i][j] += triangle[i-1][j]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

    return max(triangle[-1])
    
    