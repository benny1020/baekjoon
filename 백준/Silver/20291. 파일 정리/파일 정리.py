"""
파일을 확장자 별로 정리해서 몇개씩 있는지 알려줘
보기편하게 확장자들을 사전순으로 정렬해줘
"""

if __name__ == "__main__":
    n = int(input())
    ex = dict()

    for i in range(n):
        f = input().split('.')[1]
        if f in ex.keys():
            ex[f] += 1
        else:
            ex[f] = 1

    ex = list(sorted(ex.items(), key=lambda x: x[0]))

    for i in ex:
        print(i[0] + ' ' + str(i[1]))
