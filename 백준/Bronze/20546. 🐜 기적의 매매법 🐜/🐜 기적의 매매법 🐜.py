"""

무조건 삼 -> BNP

3일 연속 내리면 사고
3일 연속 오르면 팜 -> TIMING
"""

if __name__ == "__main__":
    money = int(input())
    stock = list(map(int, input().split(' ')))


    # BNP
    bmoney = money
    bnum = 0
    for s in range(len(stock)):
        if bmoney >= stock[s]:
            tmp = (bmoney // stock[s])
            bnum += tmp
            bmoney -= (tmp * stock[s])

    up_day = 0
    down_day = 0
    tmoney = money
    tnum = 0
    for s in range(1,len(stock)):
        if stock[s] > stock[s-1]:
            up_day += 1
            down_day = 0
        elif stock[s] < stock[s-1]:
            up_day = 0
            down_day += 1

        else:
            up_day = 0
            down_day = 0

        if up_day >= 3:
            tmoney += (stock[s] * tnum)
            tnum = 0

        if down_day >= 3:
            if tmoney >= stock[s]:
                tmp = (tmoney // stock[s])
                tnum += tmp
                tmoney -= (tmp * stock[s])

    tmoney += tnum*stock[-1]
    bmoney += bnum*stock[-1]

    #print(tmoney)
    #print(bmoney)

    if tmoney > bmoney:
        print("TIMING")
    elif tmoney < bmoney:
        print("BNP")
    else:
        print("SAMESAME")




