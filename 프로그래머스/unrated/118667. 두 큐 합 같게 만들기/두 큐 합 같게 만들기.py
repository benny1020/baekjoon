# 3 2 7 2 | 4 6 5 1 |
from collections import deque

def solution(queue1, queue2):
    
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    cnt = 0
    
    for i in range(len(queue1)*3):
        if(sum1 == sum2):
            return cnt
        
        if(sum1 > sum2):
            num = queue1.popleft()
            #num = queue1.pop(0)
            #queue2.append(num)
            queue2.append(num)
            sum1 -= num
            sum2 += num
        else:
            #num = queue2.pop(0)
            #queue1.append(num)
            num = queue2.popleft()
            queue1.append(num)
            sum2 -= num
            sum1 += num
            
        cnt+=1
    
    return -1
            
                           

