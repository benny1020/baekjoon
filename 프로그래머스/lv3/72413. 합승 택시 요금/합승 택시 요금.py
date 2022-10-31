def solution(n, s, a, b, fares):
    INF = 100000001
    cost = [[0 for i in range(n+1)] for j in range(n+1)]

    
    for fare in fares:
        cost[fare[0]][fare[1]] = fare[2]
        cost[fare[1]][fare[0]] = fare[2]

    """
    # ----------
    # s -> a + s -> b
    q = [s]
    case = [INF for j in range(n+1)]
    case[s] = 0
    visit = [False for i in range(n+1)]
    visit[s] = True

    while len(q) != 0:
        cur = q.pop(0)

        for v in info[cur]:
            if case[v] > case[cur] + cost[cur][v]:
                case[v] = case[cur] + cost[cur][v]
            if not visit[v]:
                q.append(v)
                visit[v] = True
    print(case)
    aplusb = case[a]+case[b]
    # ------
    """
        
    # 합승 후 따로가기

    case = cost
    for i in range(n+1):
        for j in range(n+1):
            if case[i][j] == 0:
                case[i][j] = INF
    for i in range(n+1):
        case[i][i] = 0
    
    for i in range(n+1):
        for j in range(n+1):
            for k in range(n+1):
                case[j][k] = min(case[j][k], case[j][i]+case[i][k])
                case[k][j] = case[j][k]
    minn = INF
    #print(case)
    for i in range(1,n+1):
        minn = min(minn, case[s][i] + case[i][b] + case[i][a])
    minn = min(minn, case[s][a]+case[s][b])
    
    
    return minn
            
    
        
    
    
    # s -> a -> b
    
    # s -> b -> a
    