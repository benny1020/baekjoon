def solution(skill, skill_trees):
    d = dict()
    for i in range(len(skill)):
        d[skill[i]] = i

    tot = 0
    
    for sk in skill_trees:
        count = [ 0 for i in range(len(skill)) ] 
        for i in range(len(sk)):
            if sk[i] in d:
                if count[d[sk[i]]] >= d[sk[i]]:
                    for key in d.keys():
                        if d[key] > d[sk[i]]:
                            count[d[key]]+=1
                else: 
                    break # 여기서 깨짐 
                
            if i == len(sk)-1:
                tot += 1
    

    return tot