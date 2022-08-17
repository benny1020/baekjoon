def solution(x):
    digit = len(str(x))
    
    tot=0
    for i in range(digit):
        tot+=int(str(x)[i])
    return x%tot==0
   