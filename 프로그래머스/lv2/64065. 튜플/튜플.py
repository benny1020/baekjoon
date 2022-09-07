def solution(s):
    s=s[1:len(s)-1]

    ans = set()
    d = dict()
    num = ""
    bli = []
    li = []
    for st in s:
        if st == "{":
            li = []
        elif st == "}":
            li.append(int(num))
            bli.append(li)
            num = ""
        elif st == ",":
            if num != "":
                li.append(int(num))
            num = ""
        else:
            num+=st
        
    bli.sort(key = lambda x : len(x))

    
    ans = []
    
    for l in bli:
        for j in l:
            if j not in ans:
                ans.append(j)
    return ans
    
    
    ans = []
    
    for l in sorted(d.items(), key = lambda x : x[1],reverse=True):
        ans.append(int(l[0]))
        
    return ans

