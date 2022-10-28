from itertools import combinations
def solution(relation):
    key = [i for i in range(len(relation[0]))]
    idx = []
    ans = []

    for i in range(1,len(relation[0])+1):
        idx.extend(list(combinations(key,i)))
    ans = set()
    for i in idx:
        rel = set()
        flag = True
        for j in range(len(relation)):
            tmp = ""
            for k in i:
                tmp += relation[j][k]
                tmp += " "
            if tmp not in rel:
                rel.add(tmp)
            else:
                flag = False
                break

        if flag:
            f = True
            for a in ans:
                if set(a) < set(i):
                    f = False
                    break
            if f:
                ans.add(i)
        
    return len(ans)
                
