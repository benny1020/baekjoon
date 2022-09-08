from collections import deque

def solution(people, limit):
    people.sort()
    people = deque(people)
    
    answer = 0
    total = 0
    
    while(people):
        total += people.pop()
        
        while(people):
            if total + people[0] <= limit:
                total += people.popleft()
            else:
                break
        
        total = 0
        answer += 1        

    return answer