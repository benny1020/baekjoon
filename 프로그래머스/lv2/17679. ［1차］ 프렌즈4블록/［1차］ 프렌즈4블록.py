def solution(m, n, board):
    answer = 0
    b = [[] for i in range(n)]
    for i in range(m):
        for j in range(n):
            b[j].append(board[i][j])
    for i in range(m):
        b[i].reverse()

    check = [[True for j in range(m)] for i in range(n)]

    dx = [1, 1, 0, 0]
    dy = [1, 0, 1, 0]

    while True:
        for i in range(n):
            for j in range(len(b[i])):
                block = b[i][j]
                count = 0
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0 <= nx < n and 0 <= ny < len(b[nx]):
                        if block == b[nx][ny]:
                            count += 1
                if count == 4:
                    for d in range(4):
                        nx = i + dx[d]
                        ny = j + dy[d]
                        check[nx][ny] = False

        flag = True

        for i in range(n):
            tmp = []
            tmp_b = []
            for j in range(len(b[i])):
                if check[i][j]:
                    tmp.append(True)
                    tmp_b.append(b[i][j])
                else:
                    answer += 1
                    flag = False
            check[i] = tmp
            b[i] = tmp_b
        if flag:
            break

    return answer