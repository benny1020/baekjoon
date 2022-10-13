import sys


def go(cur, dep, visitt, graph, nn):
    if dep >= 4:
        return True
    for k in graph[cur]:
        if k == cur:
            continue
        if not visitt[k]:
            visitt[k] = True
            if go(k, dep + 1, visitt, graph, nn):
                return True
            visitt[k] = False

    return False


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    g = [[] for j in range(n)]

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        g[a].append(b)
        g[b].append(a)

    visit = [False for j in range(n)]
    for i in range(n):
        visit[i] = True
        if go(i, 0, visit, g, n):
            print(1)
            exit(0)
        visit[i] = False

    print(0)
    # 1 7 3 4 6
