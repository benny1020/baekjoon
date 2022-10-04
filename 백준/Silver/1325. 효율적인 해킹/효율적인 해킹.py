"""
신뢰하는 관계, 신뢰하지 않는 관계
A가 B를 신뢰하는 경우 B를 해킹하면 A도 해킹할 수 있다.

한번에 가장 많은 컴퓨터를 해킹할 수 있는 번호
bfs로 타고 내려가다가 가장 큰
"""
import collections
import time
import sys

if __name__ == "__main__":
    start = time.time()

    n, m = map(int, input().split())

    g = [set() for j in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        g[b].add(a)

    max_num = 0
    max_list = []

    check = dict()

    for i in range(1, n + 1):
        q = collections.deque()
        q.append(i)
        visit = [False for j in range(n+1)]
        visit[i] = True
        # visit = set()
        # visit.add(i)
        num = 1
        while len(q) != 0:
            t = q.popleft()
            for c in g[t]:
                # if c not in visit:
                if not visit[c]:
                    num += 1
                    q.append(c)
                    # visit.add(c)
                    visit[c] = True

        if num > max_num:
            max_list.clear()
        if num >= max_num:
            max_num = num
            max_list.append(i)

    for k in max_list:
        print(k, end=' ')

    # print(time.time() - start)
