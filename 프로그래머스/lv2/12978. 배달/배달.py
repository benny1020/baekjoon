"""
N개의 마을, 양방향으로 통행할 수 있는 도로로 연결
a, b, c
a마을과 b마을을 연결하는데 걸리는 시간은 c
K는 음식 배달이 가능한 시간
1번 마을에 있는 음식점이 K이하의 시간에 배달이 가능한 마을의 개수
DFS? 이거 그냥
"""
def solution(N, road, K):
    MAX_NUM = 999999
    cost = [[MAX_NUM for i in range(N+1)] for j in range(N+1)]
    info = [set() for i in range(N+1)]
    
    
    for r in road:
        cost[r[0]][r[1]] = min(r[2],cost[r[0]][r[1]])
        cost[r[1]][r[0]] = min(r[2],cost[r[0]][r[1]])
        
        
        info[r[0]].add(r[1])
        info[r[1]].add(r[0])

        
    visit = [ MAX_NUM for i in range(N+1)]
    visit[1] = 0
    q = [[1]] # 현재 위치와 비용
    
    while len(q) != 0:
        num = q.pop()
        for s in info[num[0]]:
            if visit[num[0]] + cost[num[0]][s] < visit[s] and visit[num[0]] + cost[num[0]][s] <= K:
                visit[s] = visit[num[0]] + cost[num[0]][s]
                q.append([s])

    print(visit)
    count = 0
    for v in range(1, len(visit)):
        if visit[v] <= K:
            count += 1
    return count

