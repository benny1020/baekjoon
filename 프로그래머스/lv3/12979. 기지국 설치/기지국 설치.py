import math
def solution(n, stations, w):
    
    cur = 0
    count = 0
    # 1 2 3 4 5 
    while cur < n:
        if len(stations) == 0:
            count += math.ceil(((n)-cur)/(2*w+1))
            break
        station = stations.pop(0)-1
        # 7 st->11 w=2  (st-w-7)
        # 유효 범위에 안들면
        if cur < station - w:
            count += math.ceil((station-w-cur)/(2*w+1))
        
        cur = station + w + 1
    return count
        
    
