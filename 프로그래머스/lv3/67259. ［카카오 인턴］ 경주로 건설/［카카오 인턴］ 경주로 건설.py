"""
N X N 
0 or 1
경주로는 상하좌우로 인접한 두 빈 칸을 연결하여 건설할 수 있으며, 벽이 있는 칸에는 경주로를 건설할 수 없습니다.
인접한 두 빈 칸을 상하 또는 좌우로 연결한 경주로를 직선도로라고한다.
두 직선 도로가 서로 직각으로 만나는 지점을 코너라고한다.
직선도로 하나 - 100원
코너 하나 - 500원
출발 0,0 ~ n,n으로 가는거
모든 길 dfs하면되지않나? 재귀로 코너 꺾이면 1
코너 조건?
0,0
1,0
1,1

"""
global minCost
global costList
minCost = 99999999

def isCorner(roads):
    if len(roads) < 3:
        return False
    else:
        if abs(roads[0][0]-roads[1][0]) != abs(roads[2][0]-roads[1][0]) or abs(roads[0][1]-roads[1][1]) != abs(roads[2][1]-roads[1][1]):
            return True
        else:
            return False

def isValid(x, y, n):
    if 0 <= x < n and 0 <= y < n:
        return True
    else:
        return False
    
def dfs(board, cur, visit, corner, straight, roads):
    
    dx = [0,0,1,-1]
    dy = [-1,1,0,0]
    n = len(board)
    
    
    if roads[0] == [0,0] and len(roads) >= 3 :
        if isCorner(roads):
            straight+=2
            corner+=1
        else:
            straight += 2
    elif roads[0] != [0,0] and len(roads) >= 3:
        if isCorner(roads):
            corner += 1
            straight += 1
        else:
            straight += 1

    # 중간 종료
    global costList
    if costList[cur[0]][cur[1]] != 0 and costList[cur[0]][cur[1]] < 500*corner+100*straight - 400:
        return
    else:
        costList[cur[0]][cur[1]] = 500*corner+100*straight

    # 종료 조건
    if cur[0] == n-1 and cur[1] == n-1:
        global minCost
        cost = corner*500 + straight*100 
        if minCost > cost:
            minCost = cost
        return
    # 다음 조건
    for i in range(4):
        nx = cur[0] + dx[i]
        ny = cur[1] + dy[i]
        if isValid(nx,ny, n) and board[nx][ny] != 1 and not visit[nx][ny]:
            visit[nx][ny] = True
            tmp = roads.copy()
            roads.append([nx,ny])
            if len(roads)>=4:
                roads.pop(0)
            dfs(board,[nx,ny], visit, corner, straight, roads)
            roads = tmp
            visit[nx][ny] = False
    return
        
    
def solution(board):

    global costList
    costList = [[0 for i in range(len(board))]for j in range(len(board))]
    
    visit = [[False for i in range(len(board))]for j in range(len(board))]
    visit[0][0] = True
    
    dfs(board, [0,0], visit,0,0,[[0,0]])
    for c in costList:
        print(c)

    global minCost
    return minCost
