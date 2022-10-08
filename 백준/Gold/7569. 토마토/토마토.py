import collections
import sys
if __name__ == "__main__":
    x, y, z = map(int, input().split())
    tomato = [[[] for i in range(y)] for j in range(z)]
    for i in range(z):
        for j in range(y):
            tomato[i][j] = list(map(int, sys.stdin.readline().split()))

    visit = [[[False for k in range(x)] for i in range(y)] for j in range(z)]
    total = 0
    q = collections.deque()
    day = 0

    dx = [0, 0, 1, -1, 0, 0]
    dy = [0, 1, 0, 0, -1, 0]
    dz = [1, 0, 0, 0, 0, -1]

    for i in range(z):
        for j in range(y):
            for k in range(x):
                if tomato[i][j][k] == 1:
                    q.append((i, j, k, 0))
                    visit[i][j][k] = True
                elif tomato[i][j][k] == 0:
                    total += 1

    while len(q) != 0:
        t = q.popleft()

        for d in range(6):
            mz = t[0] + dz[d]
            my = t[1] + dy[d]
            mx = t[2] + dx[d]

            if 0 <= mx < x and 0 <= my < y and 0 <= mz < z and not visit[mz][my][mx] and tomato[mz][my][mx] == 0:
                q.append((mz, my, mx, t[3] + 1))
                if day <= t[3] + 1:
                    day = t[3] + 1
                visit[mz][my][mx] = True
                total -= 1
    if total == 0:
        print(day)
    else:
        print(-1)
