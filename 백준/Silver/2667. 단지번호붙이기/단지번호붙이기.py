import collections
if __name__ == "__main__":
    n = int(input())
    m = []
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    for _ in range(n):
        m.append(input())

    visit = [[False for i in range(n)] for j in range(n)]

    ans = []

    for i in range(n):
        for j in range(n):
            if visit[i][j]:
                continue
            if m[i][j] == '0':
                continue
            q = collections.deque()
            q.append([i, j])
            num = 1
            visit[i][j] = True
            while len(q) != 0:
                t = q.pop()

                for k in range(4):
                    nx = t[0] + dx[k]
                    ny = t[1] + dy[k]
                    if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny] and m[nx][ny] == '1':
                        visit[nx][ny] = True
                        q.append([nx, ny])
                        num += 1

            ans.append(num)
    ans = sorted(ans, reverse=False)

    print(len(ans))
    for a in ans:
        print(a)

