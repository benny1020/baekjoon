if __name__ == "__main__":
    n, m = map(int, input().split())

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    mapp = [[] for i in range(n)]
    ans = [[0 for j in range(m)] for i in range(n)]

    for i in range(n):
        mapp[i] = list(map(int, input().split()))

    target_x = 0
    target_y = 0
    for i in range(n):
        for j in range(m):
            if mapp[i][j] == 2:
                target_x = i
                target_y = j
    q = [[target_x, target_y]]

    visit = [[False for j in range(m)] for i in range(n)]

    visit[target_x][target_y] = True

    while len(q) != 0:
        point = q.pop(0)
        for i in range(4):
            mx = point[0] + dx[i]
            my = point[1] + dy[i]

            if 0 <= mx < n and 0 <= my < m and not visit[mx][my] and mapp[mx][my] == 1:
                ans[mx][my] = ans[point[0]][point[1]] + 1
                visit[mx][my] = True
                q.append([mx, my])

    for i in range(n):
        for j in range(m):
            if mapp[i][j] == 1 and ans[i][j] == 0:
                ans[i][j] = -1
            print(ans[i][j], end=' ')
        print("")
