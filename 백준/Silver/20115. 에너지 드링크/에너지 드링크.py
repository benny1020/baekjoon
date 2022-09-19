"""
1. 임의의 서로 다른 두 에너지 드링크를 고른다.
2. 한쪽 다른쪽 모두 붓는데 반만 들어감
제일 작은 양을 큰 쪽에 버려야 함 -> 양방향 -> deque 사용
제일 큰거 빼고 나머지 작은것들 /2 해서 더하기

"""
if __name__ == "__main__":
    n = int(input())
    energy = list(map(int, input().split(' ')))

    energy = sorted(energy)
    for i in range(len(energy)-1):
        energy[len(energy)-1] += round(energy[i]/2, 5)
        energy[len(energy)-1] = round(energy[len(energy)-1],5)

    print(energy[len(energy)-1])

