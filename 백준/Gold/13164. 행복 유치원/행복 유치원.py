"""
N명의 원생들을 키 순서대로 일렬로 줄 세우고, 총 K개의 조로 나눈다
각 조에는 원생이 적어도 한명 이상
같은 조에 속 한 원생들은 서로 인접
조별로 인원수 같을 필요 X
티셔츠 비용 -> 키가 큰 원생과 작은 원생 차이
비용 최소

N-> 원생 수
K -> 조
최대한 비슷한 애들 끼리 배정
N / K 만큼 배정 나머지는?
1 3 5 6 10

2 2 1 4


4 2 2 1

5 6
1 3
10



3개 조

3 100 200 202 204 -> 4

3개 조
2 2 97 100


97 100 2 2

차이가 크게 되는것을 혼자 놔둬

2 2 1 4
"""

if __name__ == "__main__":

    n, k = map(int, input().split(' '))
    st = list(map(int, input().split(' ')))
    st = sorted(st)
    li = []
    for i in range(len(st)-1):
        li.append(st[i+1]-st[i])

    print(sum(sorted(li)[:n-k]))


