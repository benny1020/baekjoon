import sys
if __name__ == "__main__":
    n, l, r = map(int, sys.stdin.readline().split())

    g = [[] for j in range(n)]

    for i in range(n):
        g[i] = list(map(int, sys.stdin.readline().split()))


    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]
    q = []
    day = 0
    while True:
        flag = False
        visit = [[False for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                if not visit[i][j]:
                    visit[i][j] = True
                    q = [[i, j]]
                    route = [[i, j]]
                    total = g[i][j]
                    while len(q) != 0:
                        t = q.pop()
                        for d in range(4):
                            mx = t[0] + dx[d]
                            my = t[1] + dy[d]
                            if 0 <= mx < n and 0 <= my < n and not visit[mx][my] and l <= abs(
                                    g[t[0]][t[1]] - g[mx][my]) <= r:
                                visit[mx][my] = True
                                q.append((mx, my))
                                route.append((mx, my))
                                total += g[mx][my]
                    if len(route) > 1:
                        for pos in route:
                            g[pos[0]][pos[1]] = int(total / len(route))
                            visit[pos[0]][pos[1]] = True
                        flag = True
        if not flag:
            break
        day += 1

    print(day)
