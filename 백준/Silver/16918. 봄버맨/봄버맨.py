"""
폭탄이 있는 칸은 3초 지난 후에 폭발,
폭탄이 폭발한 이후에는 폭탄이 있던 칸이 파괴되어 빈칸이 되며
인접한 네칸도 함께 폭발

일부 칸에 폭탄 설치
1초동안 아무것도안함 1초
1초동안 모든 칸에 폭탄설치 2초
1초 지난 후에 3초전에 폭탄이 모두 폭발 3초
"""

if __name__ == "__main__":
    r, c, n = map(int, input().split())
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    # 1초 전체 폭탄
    # 2초

    m = []
    for _ in range(r):
        m.append(input())

    if n == 1:
        for t in m:
            print(t)
        exit(0)
    k=0
    if n % 2 == 0:
        k=3
    elif (n//2) % 2 == 1:
        k=4
    else:
        k=6
    for i in range(2, k):
        if i % 2 == 0: # 전체 0
            for a in range(r):
                for b in range(c):
                    if m[a][b] == 'O':
                        m[a] = m[a][:b] + '2' + m[a][b+1:]
                    else:
                        m[a] = m[a][:b] + 'O' + m[a][b+1:]

        else: # 0 처음꺼 터짐 그리고 나머지 0
            for a in range(r):
                for b in range(c):
                    if m[a][b] == '2':
                        m[a] = m[a][:b] + '.' + m[a][b+1:]
                        for k in range(4):
                            mx = a + dx[k]
                            my = b + dy[k]
                            if 0 <= mx < r and 0 <= my < c and m[mx][my] != '2':
                                m[mx] = m[mx][:my] + '.' + m[mx][my+1:]
    for i in range(r):
        for j in range(c):
            if m[i][j] == '2':
                m[i] = m[i][:j] + 'O' + m[i][j+1:]
    for t in m:
        print(t)



"""
6 7 3
.......
...O...
....O..
.......
OO.....
OO.....
"""