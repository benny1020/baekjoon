import sys
from collections import deque
if __name__ == "__main__":
    n, m, tt = map(int, sys.stdin.readline().split())
    castle = [[] for i in range(n)]

    visit = [[n * m for i in range(m)] for j in range(n)]
    sword = [[False for i in range(m)] for j in range(n)]

    for i in range(n):
        castle[i] = list(map(int, sys.stdin.readline().split()))
        for j in range(len(castle[i])):
            if castle[i][j] == 2:
                lx = i
                ly = j

    q = deque([(0, 0)])
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    visit[0][0] = 0

    while len(q) != 0:
        t = q.popleft()
        if castle[t[0]][t[1]] == 2:
            sword[t[0]][t[1]] = True

        for i in range(4):
            nx = t[0] + dx[i]
            ny = t[1] + dy[i]

            if 0 <= nx < len(castle) and 0 <= ny < len(castle[0]):
                # has sword
                if sword[t[0]][t[1]]:
                    if visit[t[0]][t[1]] + 1 <= tt and visit[t[0]][t[1]] + 1 < visit[nx][ny]:
                        visit[nx][ny] = visit[t[0]][t[1]] + 1
                        sword[nx][ny] = True
                        q.append((nx,ny))
                else:
                    if visit[t[0]][t[1]] + 1 <= tt and visit[t[0]][t[1]] + 1 < visit[nx][ny] and castle[nx][ny] != 1:
                        visit[nx][ny] = visit[t[0]][t[1]] + 1
                        q.append((nx, ny))

    toPrincess = visit[n-1][m-1]
    toSword = visit[lx][ly]
    visit = [[n * m for i in range(m)] for j in range(n)]
    q = deque([(lx, ly)])
    visit[lx][ly] = 0
    while len(q) != 0:
        t = q.popleft()

        for i in range(4):
            nx = t[0] + dx[i]
            ny = t[1] + dy[i]

            if 0 <= nx < len(castle) and 0 <= ny < len(castle[0]):
                # has sword
                if visit[t[0]][t[1]] + 1 <= tt and visit[t[0]][t[1]] + 1 < visit[nx][ny]:
                    visit[nx][ny] = visit[t[0]][t[1]] + 1
                    sword[nx][ny] = True
                    q.append((nx, ny))

    sword_to_princess = visit[n-1][m-1]
    if toPrincess == n*m:
        if toSword != n*m and toSword+sword_to_princess <= tt:
            print(toSword+sword_to_princess)
        else:
            print("Fail")
        exit(0)

    ans = min(toPrincess,toSword+sword_to_princess)
    print(ans)








