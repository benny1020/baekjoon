def solution(msg):
    loc = 0
    ans = []
    d = dict()
    for i in range(1,27):
        d[chr(ord('A')-1 + i)] = i
        
    
    tmp = ""
    loc = 0
    for loc in range(len(msg)):
        w = tmp + msg[loc]
        if loc+1 == len(msg):
            c=""
        else:
            c = msg[loc+1]
        
        if w+c in d.keys():
            tmp = w
        else:
            tmp = ""
            d[w+c] = len(d)+1
            ans.append(d[w])
    if tmp != "":
        if tmp in d.keys():
            ans.append(d[tmp])
        else:
            ans.append(len(d)+1)
    return ans