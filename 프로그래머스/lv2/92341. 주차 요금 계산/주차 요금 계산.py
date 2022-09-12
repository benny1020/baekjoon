import math
def solution(fees, records):
    f = dict()
    car = dict()
    li=[]
    for record in records:
        time, carNum, s = record.split(' ')
        hour, minutes = time.split(':')
        hour = int(hour)
        minutes = int(minutes)
        if carNum not in car:
            car[carNum] = int(hour*60 + minutes)
        else:

            partTime = int(hour*60+minutes) - int(car[carNum])


            if carNum in f:
                f[carNum] += partTime
            else:
                f[carNum] = partTime
            del car[carNum]
    


    for c in car:
        partTime = int(60*23+59 - car[c])
        if c in f:
            f[c] += partTime
        else:
            f[c] = partTime

    ans = dict()
    for cn in f:
        if f[cn] <= fees[0]:
            ans[cn] = fees[1]
        else:
            ans[cn] = fees[1] + math.ceil( (f[cn] - fees[0]) / fees[2] )*fees[3]
            
    
    ans = list(sorted(ans.items()))
    a = []
    for i in ans:
        a.append(i[1])
    return a
                
            