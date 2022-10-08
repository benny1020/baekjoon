"""
보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은
익은 토마토들은 익은 토마토들의 영향을 받아 익게된다
대각선은 영향을 못줌

"""
import collections
if __name__ == "__main__":
    n, m = map(int, input().split())
    tomato = [[] for i in range(m)]
    for i in range(m):
        tomato[i] = list(map(int, input().split()))

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    total = 0
    visit = [[False for i in range(n)] for j in range(m)]
    q = collections.deque()
    for i in range(m):
        for j in range(n):
            if tomato[i][j] == 1:
                q.append((i, j, 0))
                visit[i][j] = True
            elif tomato[i][j] == 0:
                total += 1
    day = 0
    while len(q) != 0:
        t = q.popleft()
        for d in range(4):
            mx = t[0] + dx[d]
            my = t[1] + dy[d]

            if 0 <= mx < m and 0 <= my < n and not visit[mx][my] and tomato[mx][my] == 0:
                q.append((mx, my, t[2] + 1))
                if day <= t[2] + 1:
                    day = t[2] + 1
                visit[mx][my] = True
                total -= 1

    if total == 0:
        print(day)
    elif total >= 0:
        print(-1)

