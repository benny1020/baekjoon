"""
N X N 크기의 격자
학교에 다니는 학생 수는 N^2

1번부터 N^2 까지 번호

r,c
r1-r2 + c1 - c2 = 1

1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
2. 1을 만족하는 칸이 여러개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
3. 2를 만족하는 칸도 여러개인 경우에는 행의 번호가 가장 작은 칸 아니면 열의 번호가 가장 작은


"""


def valid(x, y, n):
    if 0 <= x < n and 0 <= y < n:
        return True
    else:
        return False


def check(seat, student, like):
    # 1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
    target = []
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    max_like = 0
    # ------------- 1단계
    for i in range(len(seat)):
        for j in range(len(seat[0])):
            # 좋아하는 사람 계산
            if seat[i][j] == 0:
                lk = 0
                for k in range(4):
                    if valid(i + dx[k], j + dy[k], len(seat)):
                        if seat[i + dx[k]][j + dy[k]] in like[student]:
                            lk += 1
                if max_like < lk:
                    target.clear()
                if max_like <= lk:
                    target.append([i, j])
                    max_like = lk
    # 타켓 하나면 종료
    if len(target) == 1:
        return target[0]
    # --------- 2단계
    # 1을 만족하는 칸이 여러 개이면 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
    empty_list = []
    max_e = 0
    for i in range(len(target)):
        e = 0
        for d in range(4):
            if valid(target[i][0] + dx[d], target[i][1] + dy[d], len(seat)):
                if seat[target[i][0] + dx[d]][target[i][1] + dy[d]] == 0:
                    e += 1
        if max_e < e:
            empty_list.clear()
        if max_e <= e:
            empty_list.append([target[i][0], target[i][1]])
            max_e = e
    # 종료 조건
    if len(empty_list) == 1:
        return empty_list[0]

    # 마지막으로 행의 번호가 가장 작거나 열의 번호가 가장 작은경우
    empty_list = sorted(empty_list, key=lambda x: (x[0], x[1]))
    return empty_list[0]


if __name__ == "__main__":

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    n = int(input())
    st_like = [[] for i in range(n ** 2 + 1)]
    st_order = []
    seats = [[0 for i in range(n)] for j in range(n)]

    for i in range(n ** 2):
        st = list(map(int, input().split(' ')))
        st_order.append(st[0])
        st_like[st.pop(0)] = st

    for st in st_order:
        s = check(seats,st,st_like)
        seats[s[0]][s[1]]=st

    ans = 0

    #----- 호감도 계산
    for i in range(len(seats)):
        for j in range(len(seats[0])):
            # 좋아하는 사람 계산
            lk = 0
            for k in range(4):
                if valid(i + dx[k], j + dy[k], len(seats)):
                    if seats[i + dx[k]][j + dy[k]] in st_like[seats[i][j]]:
                        lk += 1
            if lk > 0:
                ans += 10**(lk-1)
    print(ans)
