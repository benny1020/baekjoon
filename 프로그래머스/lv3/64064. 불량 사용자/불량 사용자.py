def isMatch(u_id, ban_id):
    if len(u_id) != len(ban_id):
        return False
    for i in range(len(u_id)):
        if ban_id[i] != '*' and u_id[i] != ban_id[i]:
            return False
    return True

# frado crodo
# fradi crodo
# fradi frodo
# frodo frodo 2 * 2 * 2 - 1 - 2 
import itertools   
def solution(user_id, banned_id):
    li = [set() for i in range(len(banned_id))]
    for i in range(len(banned_id)):
        for j in range(len(user_id)):
            if isMatch(user_id[j], banned_id[i]):
                li[i].add(j)
    uid = [i for i in range(len(user_id))]
    nPr = itertools.permutations(uid,len(banned_id))
    answer=[]
    count = 0
    for i in nPr:
        for j in range(len(banned_id)):
            if i[j] not in li[j]:
                break
            if j == len(banned_id)-1:
                tmp = list(sorted(i))
                if tmp not in answer:
                    answer.append(tmp)

    
    return len(answer)
                