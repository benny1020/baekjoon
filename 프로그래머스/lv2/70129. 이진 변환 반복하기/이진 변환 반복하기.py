def toBinary(num):
    digit = 0
    while(num >= 2**digit):
        digit+=1

    s=""
    for i in reversed(range(digit)):
        if 2**i <= num:
            num -= 2**i
            s+='1'
        else:
            s+='0'
    return s
def solution(s):
    zeroNum = 0
    trial = 0
    while(s != '1'):
        trial += 1
        i=0
        while(i<len(s)):
            if s[i] == '0':
                s = s[:i] + s[i+1:]
                zeroNum +=1
            else:
                i+=1
        s = toBinary(len(s))

    return [trial,zeroNum]