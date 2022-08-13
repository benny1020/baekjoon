def solution(price, money, count):
        
    total = (count*(count+1))/2 * price
    
    
    
    if money > total:
        return 0
    return total - money

# 3 6 9 12   20 ->   (4*3/2)*3
# 1 2 3 4    (4*5)/2 *3