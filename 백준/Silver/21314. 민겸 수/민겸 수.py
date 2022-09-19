"""
0이상 정수 N에 대해 10^N or 5 X 10^N 꼴의 십진수를 대문자 M과 K로 이루어진 문자열로 표기한다.
10^N 꼴의 십진수는 N+1개의 M으로,5 X 10^N 꼴의 십진수는 N개의 M뒤에 1개의 K를 이어붙인 문자열로 나타낸다

최소 -> M 따로 K 따로 계산
최대 -> MK최대한 묶어야함
최대 문자열 3000조심
"""

if __name__ == "__main__":
    number = str(input())
    minn = ""
    maxx = ""

    # 최소부터 구해보자
    m = 0
    cur = number[0]

    for i in range(len(number)):
        if number[i] == 'K':
            if m != 0:
                # minn += str(10 ** (m - 1))
                minn += '1'
                if m > 1:
                    for k in range(m - 1):
                        minn += '0'
                m = 0
            minn += '5'
        else:
            m += 1
    if m != 0:
        # minn += str(10 ** (m - 1))
        # minn += str(10 ** (m - 1))
        minn += '1'
        if m > 1:
            for k in range(m - 1):
                minn += '0'

    # 최대 구해보자
    m = 0
    cur = number[0]

    for i in range(len(number)):
        if number[i] == 'K':
            # maxx += str(5 * 10 ** m)
            maxx += '5'
            for j in range(m):
                maxx += '0'
            m = 0
        else:  #
            m += 1
    if m != 0:
        # minn += str(10 ** (m - 1))
        # minn += str(10 ** (m - 1))
        for k in range(m):
            maxx += '1'
        

    print(maxx + '\n' + minn)
