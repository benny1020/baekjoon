

def go(numbers,current,total,target):
    global ans
    if current == len(numbers):
        if total == target:
            ans += 1
    else:
        go(numbers,current+1,total+numbers[current],target)
        go(numbers,current+1,total-numbers[current],target)
    

def solution(numbers, target):
    global ans
    ans=0
    go(numbers,0,0,target)
    return ans