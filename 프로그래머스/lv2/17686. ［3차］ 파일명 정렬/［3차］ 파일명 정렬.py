"""
head 순
number 순
원래 입력 순
"""
from functools import cmp_to_key
def compare(x, y):
    xhead, xnumber = '', ''
    yhead, ynumber = '', ''
    xflag, yflag = 1, 1
    for i in range(len(x)):
        if x[i].isnumeric():
            if xflag:
                xhead = x[:i]
                xnumber = x[i]
                xflag = 0
            else: xnumber += x[i]
        else:
            if xflag == 0:
                break
    for j in range(len(y)):
        
        if y[j].isnumeric():
            if yflag:
                yhead = y[:j]
                ynumber = y[j]
                yflag = 0
            else: ynumber += y[j]
        else:
            if yflag == 0:
                break
    # ------
    
    if xhead.lower() == yhead.lower():
        if int(xnumber) == int(ynumber):
            return 0
        elif int(xnumber) < int(ynumber):
            return -1
        elif int(xnumber) > int(ynumber):
            return 1
    elif xhead.lower() < yhead.lower():
        return -1
    elif xhead.lower() > yhead.lower():
        return 1
def solution(files):
    return sorted(files, key=cmp_to_key(compare))