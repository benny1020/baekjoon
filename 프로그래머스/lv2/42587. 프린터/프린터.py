from collections import deque
def solution(priorities, location):
    priorities = deque(priorities)
    trial = 0
    while(True):
        tmp = priorities.popleft()
        if len(priorities) > 1 and tmp < max(priorities)  : #뒤로 넘어갈때
            priorities.append(tmp)
            if location == 0:
                location = len(priorities) -1
            else:
                location -= 1
        else:
            if location == 0:
                return trial+1
            else:
                location -= 1
                trial +=1
            
    answer = 0
    return answer