from collections import deque
def solution(topping):

    answer = 0
    topping = deque(topping)
    rightToppingCount = dict()
    leftToppingCount = dict()
    
    leftToppingSet = set()
    rightToppingSet = set(topping)
    
    for top in topping:
        rightToppingCount[top] = 0
        leftToppingCount[top] = 0
        
    for top in topping:
        rightToppingCount[top] += 1
        
    while len(topping) != 0:
        top = topping.popleft()
        leftToppingCount[top] += 1
        leftToppingSet.add(top)
        
        rightToppingCount[top] -= 1
        if rightToppingCount[top] == 0:
            rightToppingSet.remove(top)
        
        if len(leftToppingSet) == len(rightToppingSet):
            answer+=1

    
    return answer