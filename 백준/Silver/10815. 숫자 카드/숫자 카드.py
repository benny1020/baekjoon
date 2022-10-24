if __name__ == "__main__":
    n = int(input())
    numbers = set(list(map(int,input().split())))

    m = int(input())
    answer = list(map(int, input().split()))
    ans = []
    for a in answer:
        if a in numbers:
            ans.append(1)
        else:
            ans.append(0)
    for i in ans:
        print(i, end=' ')
