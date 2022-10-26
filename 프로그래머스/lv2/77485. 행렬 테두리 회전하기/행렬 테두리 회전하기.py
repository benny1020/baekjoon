"""
직사각형 한칸씩

시계방향 회전

"""
from collections import deque

def rotate(m,query):
    numbers = deque()
    # 세로 2 2 5 4
    height = query[2] - query[0] + 1
    width = query[3] - query[1] + 1
    start = [query[0]-1,query[1]-1]
    
    
    
    for i in range(width-1):
        numbers.append(m[start[0]][start[1]])
        start[1]+=1
        
    for i in range(height-1):
        numbers.append(m[start[0]][start[1]])
        start[0]+=1
    
    for i in range(width-1):
        numbers.append(m[start[0]][start[1]])
        start[1]-=1
        
    for i in range(height-1):
        numbers.append(m[start[0]][start[1]])
        start[0]-=1
    
    numbers.appendleft(numbers.pop())
    
    start = [query[0]-1,query[1]-1]
    
    num = 0
    for i in range(width-1):
        m[start[0]][start[1]] = numbers[num]
        num+=1
        start[1]+=1
        
    for i in range(height-1):
        m[start[0]][start[1]] = numbers[num]
        num+=1
        start[0]+=1
    
    for i in range(width-1):
        m[start[0]][start[1]] = numbers[num]
        num+=1
        start[1]-=1
        
    for i in range(height-1):
        m[start[0]][start[1]] = numbers[num]
        num+=1
        start[0]-=1
    
    return m, min(numbers)

def solution(rows, columns, queries):
    m = [[i*columns+j+1 for j in range(columns)] for i in range(rows)]
    ans = []
    
    for query in queries:
        m, minn = rotate(m, query)

        ans.append(minn)
    return ans
    