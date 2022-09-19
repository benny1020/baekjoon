"""
PT 받을때 운동기구 최대 2개 선택

N개 운동기구 한번씩
근손실 최소

정렬 후
N이 짝수인경우 제일작은것과 큰것 합
홀수인경우
제일 큰거 빼고 짝수인것저처럼 ㄱ ㄱ

"""

if __name__ == "__main__":
    n = int(input())

    muscle = list(map(int, input().split(' ')))

    muscle = sorted(muscle)

    if len(muscle) == 1:
        print(muscle[0])
        exit(0)

    ans = muscle[-1] + muscle[0]

    if len(muscle) % 2 == 1:  # 홀수인 경우
        ans = muscle.pop()

    for i in range(int(len(muscle) / 2)):
        if ans <= muscle[i] + muscle[len(muscle) - i - 1]:
            ans = muscle[i] + muscle[len(muscle) - i - 1]

    print(ans)
