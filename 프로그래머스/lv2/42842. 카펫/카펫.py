def solution(brown, yellow):
    y = []
    c = []
    
    for i in range(1,yellow+1):
        if yellow%i == 0:
            y.append([i,yellow/i])

    for i in range(1,brown+yellow+1):
        if (brown+yellow)%i == 0:
            c.append([i,(brown+yellow)/i])

    
    for i in y:
        for j in c:
            if (min(j) - min(i) ) % 2 == 0 and (max(j) - max(i) ) % 2 == 0:
                
                if min(j) > 1 and max(j)> max(i) and min(j) > min(i):
                    return [max(j),min(j)]
        