def convert(n,k):
    i = 0
    ans = ""
    while k**i <= n:
        i+=1
    for j in reversed(range(0,i)):
        if n >= (k**j):
            ans += str(int(n/(k**j)))
            n = n - int(n/(k**j))*(k**j)
        else:
            ans += "0"
    return ans
def solution(n, k):
    ch = set()
    cv = convert(n, k)
    q = ""
    count = 0
    for i in range(len(cv)):
        if cv[i] == '0':
            if q != "":
                if int(q) in ch or prime_check(int(q)):
                    ch.add(int(q))
                    count += 1
                q = ""
        else:
            q += cv[i]

    if q != "" and prime_check(int(q)):
        count += 1
    return count
def prime_check(num):
    if num == 0 or num == 1:
        return False
    #for i in range(2,(num//2)+1):
    for i in range(2,int(num**(1/2))+1):

        if num % i == 0:
            return False
    return True