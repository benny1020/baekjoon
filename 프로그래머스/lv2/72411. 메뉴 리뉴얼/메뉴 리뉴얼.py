from itertools import combinations
"""
최소 2가지 이상의 단품메뉴로 구성
최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합

course -> 스카피가 추가하고싶어하는 코스요리를 구성하는 단품메뉴들의 갯수

스카피가 새로 추가하게될 코스 요리의 메뉴 구성
"""

def solution(orders, course):


    orderList = []
    ans = []
    
    for order in orders:
        orderList.append(list(order))
        
    for c in course:
        d = dict()
        for order in orders:
            for l in list(combinations(order,c)):
                w = "".join(sorted(l))
                if w in d.keys():
                    d[w] += 1
                else:
                    d[w] = 1
        res = sorted(d.items(), key = lambda d : d[1], reverse = True)
        for r in res:
            if r[1] == res[0][1] and r[1] >= 2 :
                ans.append(r[0])
            else:
                break
    return sorted(ans)
                
    
"""
def solution(orders, course):
    orderList = []
    menu = set()
    res = []
    
    for order in orders:
        orderList.append(list(order))
        for o in list(order):
            menu.add(o)
    
    for i in course:
        combination = list(combinations(menu,i))
        num = 0
        maxx_list=[]
        maxx_num = 0
        for com in combination:
            num = 0
            for o in orderList:
                o = set(o)
                flag = True
                for c in com:
                    if c not in o:
                        flag = False
                        break
                if flag == True:
                    num+=1
            if maxx_num < num:
                maxx_num = num
                maxx_list = [com]
            elif maxx_num == num:
                maxx_list.append(com)
        if maxx_num >=2:
            res.extend(maxx_list)
        
    ans = []
    for r in res:
        a = ""
        for i in sorted(r):
            a += i
        ans.append(a)
    return sorted(ans)
            
"""       
    
