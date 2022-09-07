from collections import deque

def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    ans = []
    
    while(len(progresses) != 0):
        # 갱신
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            
        # complete 확인
        num = 0
        while(len(progresses) > 0 and progresses[0] >= 100):
            num+=1
            progresses.popleft()
            speeds.popleft()
        
        if num != 0:
            ans.append(num)
        num+=1
        
    return ans