
def binarySearch(li, target):
    left = 0
    right = len(li)-1
    while left<=right:
        #print(left,right)
        cur = (right+left)//2
        if li[cur] < target and li[cur+1] >= target:
            return cur
        if li[cur] >= target:
            right = cur-1
        else:
            left = cur+1
    return left
"""
4
1 3 4 6 8 9

left right mid
0 5 2
0 1

"""
def solution(info, query):
    #li = [1,3,4,6,8,9]
    #target = 4
    #return binarySearch(li,target)
    language_list = ["cpp", "java", "python"]
    job_list = ["backend", "frontend"]
    career_list = ["junior", "senior"]
    food_list = ["chicken", "pizza"]
    
    info_list = dict()
    answer=[]
    
    for l in language_list:
        for j in job_list:
            for c in career_list:
                for f in food_list:
                    info_list[l+' '+j+' '+c+' '+f] = []

    
    for i in info:
        li = i.split(' ')
        info_list[' '.join(li[:4])].append(int(li[-1]))
    
    for l in language_list:
        for j in job_list:
            for c in career_list:
                for f in food_list:
                    info_list[l+' '+j+' '+c+' '+f]=sorted(info_list[l+' '+j+' '+c+' '+f])

    for q in query:
        ask = []
        li = q.split(' and ')
        li[-1], score = li[-1].split(' ')
        score = int(score)
        l = []
        j = []
        c = []
        f = []
        if li[0] == '-':
            l = language_list
        else:
            l.append(li[0])
        if li[1] == '-':
            j = job_list
        else:
            j.append(li[1])
        if li[2] == '-':
            c = career_list
        else:
            c.append(li[2])
        if li[3] == '-':
            f = food_list
        else:
            f.append(li[3])
        for a in l:
            for b in j:
                for d in c:
                    for k in f:
                        ask.append(a+' '+b+' '+d+' '+k)
        count = 0
        for a in ask:
            tmp = len(info_list[a])
            if tmp == 0:
                continue
            if info_list[a][0] >= score:
                count += tmp
                continue
            if info_list[a][-1] < score:
                continue
            
            count+=(tmp - binarySearch(info_list[a],score)-1)
                
        answer.append(count)
    
    return answer
# 7 8 9 10



"""
            
cpp  java python

backend frontend

junior senior

chicken pizza



def solution(info, query):
    language_list = ["cpp", "java", "python","-"]
    job_list = ["backend", "frontend","-"]
    career_list = ["junior", "senior","-"]
    food_list = ["chicken", "pizza","-"]
    
    lang_dict = dict()
    job_dict = dict()
    career_dict = dict()
    food_dict = dict()
    codingtest = []
    all_list = set()
    ans = []
    
    for l in language_list:
        lang_dict[l] = set()
    for j in job_list:
        job_dict[j] = set()
    for c in career_list:
        career_dict[c] = set()
    for f in food_list:
        food_dict[f] = set()
    
    for i in range(len(info)):
        lang_dict["-"].add(i)
        job_dict["-"].add(i)
        career_dict["-"].add(i)
        food_dict["-"].add(i)
        
        lang, job, career, food, score = info[i].split(' ')
        lang_dict[lang].add(i)
        job_dict[job].add(i)
        career_dict[career].add(i)
        food_dict[food].add(i)
        codingtest.append(score)
    
    for i in range(len(query)):
        lang, job, career, food = query[i].split(' and ')
        food, score = food.split(' ')
        intersection = list(lang_dict[lang] & job_dict[job] & career_dict[career] & food_dict[food])
        if score == '-':
            ans.append(len(intersection))
        else:
            count = 0
            for i in intersection:
                if int(codingtest[i]) >= int(score):
                    count += 1
            ans.append(count)
            
    return ans"""
