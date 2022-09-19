"""
해결한 경우 파란색
못한 경우 빨간색

전체를 가장 많이 칠해야되는 색으로 하고
그다음에 고

"""

if __name__ == "__main__":
    n = int(input())
    color = str(input())

    cur = color[0]
    r_num = 0
    b_num = 0
    if cur == 'R':
        r_num += 1
    else:
        b_num += 1

    for i in range(1,len(color)):
        if cur == color[i]:
            continue
        else:
            cur = color[i]
            if color[i] == 'R':
                r_num += 1
            else:
                b_num += 1

    if b_num > r_num:
        print(r_num + 1)
    else:
        print(b_num + 1)
