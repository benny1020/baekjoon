"""
9 9 4 1 4 9 9
N개의 장소
연한 회색 -> 벌
진한 회색 벌통
두마리 벌은 똑바로 날아가면서 모든 칸에 꿀 딴다
숫자 -> 꿀양
두마리가 모두 지나간 장소에서는 두마리 모두 표시된 양만큼 꿀을 딴다.
시작한장소에서는 어떤 벌도 꿀 못딴다
무조건 오른쪽으로만 가능

"""

if __name__ == "__main__":

    n = int(input())
    honey = list(map(int, input().split(' ')))

    if n == 3:
        print(max(honey)*2)
        exit(0)

    max_honey = 0

    # 꿀통이 왼쪽에 있는 경우 첫번째 벌 맨 오른쪽 고정
    h = sum(honey) - honey[-1]
    for i in range(1, n-1): # 두번째 벌의 위치
        h += honey[i-1]
        #for j in range(i):
        #    h += honey[j]
        h -= honey[i]
        if max_honey < h:
            max_honey = h
        h += honey[i]

    # 꿀통이 오른쪽에 있는 경우 첫번째 벌 맨 왼쪽 고정
    h = sum(honey) - honey[0]
    for i in range(1, n):
        h += honey[i]

    for i in range(1, n-1): # 두번째 벌의 위치
        h -= honey[i]*2
        if max_honey < h:
            max_honey = h
        h += honey[i]

    print(max_honey)



