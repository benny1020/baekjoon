from collections import Counter
def solution(n):
    v = Counter(bin(n)[2:])['1']
    while n <= 1000000:
        n += 1
        p = Counter(bin(n)[2:])['1']
        if v == p:
            break
    return n