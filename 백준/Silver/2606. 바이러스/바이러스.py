if __name__ == "__main__":
    n = int(input())
    num = int(input())

    connect = [[False for i in range(n+1)] for j in range(n+1)]
    visit = [False for i in range(n+1)]

    for i in range(num):
        c1, c2 = map(int, input().split(' '))
        connect[c1][c2] = True
        connect[c2][c1] = True

    q = [1]
    ans = 0
    visit[1] = True

    while len(q) != 0:
        vi = q.pop()
        for i in range(1, n+1):
            if connect[vi][i] and not visit[i]:
                q.append(i)
                visit[i] = True
                ans += 1
    print(ans)





