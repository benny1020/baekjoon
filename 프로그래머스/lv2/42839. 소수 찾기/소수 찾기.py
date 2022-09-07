from itertools import permutations
def isPrime(num):
    if num == 1 or num == 0:
        return False
    for i in range(2,num-1):
        if num % i == 0 :
            return False
    return True

def solution(numbers):
    ans = 0
    li = []
    se = set()
    
    
    for s in numbers:
        li.append(int(s))
    
    li.sort()
    
    for i in range(1,len(numbers)+1):
        for j in permutations(li,i):
            num = 0
            for p in range(len(j)):
                num += 10**(len(j)-p-1)*j[p]
                
            if isPrime(num) == True and num not in se:
                ans+=1    
                se.add(num)
            
    return ans