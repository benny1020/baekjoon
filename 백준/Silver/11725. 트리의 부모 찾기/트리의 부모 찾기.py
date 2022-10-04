import collections
import sys
import time
if __name__ == "__main__":
    start = time.time()
    n = int(sys.stdin.readline())

    g = [set() for j in range(n + 1)]

    visit = [False for i in range(n + 1)]

    p = [0 for _ in range(n + 1)]

    for i in range(n - 1):
        a, b = map(int, sys.stdin.readline().split())
        g[a].add(b)
        g[b].add(a)

    q = collections.deque()
    q.append(1)
    visit[1] = True

    while len(q) != 0:
        t = q.popleft()
        for j in g[t]:
            if not visit[j]:
                p[j] = t
                q.append(j)
                visit[j] = True

    for i in range(2, n + 1):
        print(p[i])

    #print(time.time() - start)