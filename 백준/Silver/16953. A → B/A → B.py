"""
정수 A를 B로 바꾸려고한다.
2를 곱한다.
1을 수의 가장 오른쪽에 추가한다. -> *10 + 1 , *100 + 10
A를 B로 바꾸는데 필요한 연산의 최솟값
"""

if __name__ == "__main__":
    a, b = map(int, input().split(' '))

    trial = 1

    while True:
        trial += 1
        if (b - 1) % 10 == 0:
            b = (b - 1) / 10
        else:
            b /= 2

        if a == b:
            print(trial)
            break

        if a > b:
            print(-1)
            break

