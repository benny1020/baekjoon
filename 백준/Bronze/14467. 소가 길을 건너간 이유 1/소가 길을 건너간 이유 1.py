

if __name__ == "__main__":
    n = int(input())
    ans = 0

    li = [[] for i in range(10)]

    for i in range(n):
        cow, direction = map(int, input().split(' '))
        if len(li[cow-1]) >= 1:
            if li[cow-1][-1] != direction:
                ans += 1
        li[cow-1].append(direction)

    print(ans)
