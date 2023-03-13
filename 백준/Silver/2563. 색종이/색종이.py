if __name__ == "__main__":
    num = int(input())
    xList = []
    yList = []

    for i in range(num):
        x, y = map(int, input().split())
        xList.append(x)
        yList.append(y)

    paper = [[0 for i in range(max(yList) + 12)] for j in range(max(xList) + 12)]

    for i in range(num):
        for a in range(xList[i], xList[i] + 10):
            for b in range(yList[i], yList[i] + 10):
                paper[a][b] = 1
    answer = 0
    for i in range(len(paper)):
        answer += sum(paper[i])

    print(answer)