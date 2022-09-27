def bingo_check(bingo):
    ans = 0
    # 대각선 체크
    l = [0, 0]
    r = [0, 4]
    l_flag = True
    r_flag = True
    for i in range(5):
        if not bingo[l[0] + i][l[1] + i]:
            l_flag = False

        if not bingo[r[0] + i][r[1] - i]:
            r_flag = False
    if l_flag:
        ans += 1
    if r_flag:
        ans += 1
    # 가로 체크
    for i in range(5):
        w_flag = True
        h_flag = True
        for j in range(5):
            w_flag &= bingo[i][j]
            h_flag &= bingo[j][i]
        if w_flag:
            ans += 1
        if h_flag:
            ans += 1
    return ans

if __name__ == "__main__":

    my_bingo = [list(map(int, input().split(' '))) for i in range(5)]

    check = [[False for i in range(5)] for j in range(5)]

    mc_bingo = [list(map(int, input().split(' '))) for i in range(5)]
    for i in range(5):
        for j in range(5):
            # 철수빙고
            for k in range(5):
                flag = False
                for p in range(5):
                    if my_bingo[k][p] == mc_bingo[i][j]:
                        check[k][p] = True
                        tmp = bingo_check(check)
                        if tmp >= 3:
                            print(i*5 + j+1)
                            exit(0)
                        flag = True
                        break
                if flag:
                    break

