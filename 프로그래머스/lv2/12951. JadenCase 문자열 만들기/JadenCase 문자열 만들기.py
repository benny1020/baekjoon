def solution(s):
    flag = True
    num = 0
    for i in range(len(s)):
        if flag == True:
            if 'a' <= s[i] <= 'z':
                s = s[:i] + s[i].upper() + s[i+1:]
            flag = False
        else:
            if 'A' <= s[i] <= 'Z':
                s = s[:i] + s[i].lower() + s[i+1:]
        if s[i] == ' ':
            flag = True

    
    return s