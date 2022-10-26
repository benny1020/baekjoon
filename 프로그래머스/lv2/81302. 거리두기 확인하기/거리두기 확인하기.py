def search(places, start):
    visit = [[False for i in range(len(places[0]))] for j in range(len(places))]
    q = [[start[0],start[1],0]]
    visit[start[0]][start[1]] = True
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    
    while len(q) != 0:
        loc = q.pop(0)
        if loc[2] >= 2:
            continue
        
        for i in range(4):
            nx = loc[0]+dx[i]
            ny = loc[1]+dy[i]
            if 0 <= nx < len(places[0]) and 0 <= ny < len(places[1]) and not visit[nx][ny] and places[nx][ny] != 'X':
                    if places[nx][ny] == 'P':
                        print(start,nx,ny)
                        return False
                    q.append([nx,ny,loc[2]+1])
                    visit[nx][ny] = True
    return True
        
    
def solution(places):
    ans = []
    for place in places:
        flag = True
        for i in range(len(place)):
            for j in range(len(place[0])):
                if place[i][j] == 'P':
                    if not search(place, [i,j]):
                        flag = False
                if not flag:
                    break
            if not flag:
                break
        if not flag:
            ans.append(0)
        else:
            ans.append(1)
    return ans
                    
