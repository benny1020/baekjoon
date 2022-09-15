"""
단순한 문자 코드 순이 아닌 파일명에 포함된 숫자를 반영한 정렬 기능
Head 부분을 기준으로 사전 순으로 정렬한다.
문자열 비교시 대소문자 구분을 하지 않는다.


HEAD 부분을 기준으로 사전순 정렬
문자열 비교시 대소문자 구분 X

HEAD 대소문자 차이 외에 같을경우, number 순으로 정렬

HEAD, NUMBER 같으면 순서 그대로
"""
from functools import cmp_to_key
def myCompare(file1, file2):
    f1 = file1
    f2 = file2
    global f
    
    file1 = file1.lower()
    file2 = file2.lower()

    
    # if file1 == file2:
    #     if f1.index(file1) > f.index(file2):
    #         return 1
    #     else:
    #         return -1

    
    
    f1Head = ""
    f2Head = ""
    for s in file1:
        if s >='0' and s <= '9':
            break
        else:
            f1Head += s
            
    for s in file2:
        if s >= '0' and s <= '9':
            break
        else:
            f2Head += s
            
    file1 = file1[len(f1Head):]
    file2 = file2[len(f2Head):]
    
    if f1Head != f2Head:
        if f1Head > f2Head:
            return 1
        else:
            return -1

    
    else:
        f1Number = ""
        f2Number = ""
        
        for s in file1:
            if s >= '0' and s <= '9':
                f1Number += s
            else:
                break
                
        for s in file2:
            if s >= '0' and s <= '9':
                f2Number += s
            else:
                break
                
        if int(f1Number) == int(f2Number):
            if f.index(f1) > f.index(f2):
                 return 1
            else:
                 return -1

        if int(f1Number) > int(f2Number):
            return 1
        else:
            return -1

                
        

    
    return f1Head
        
            
    
    
    
    

def solution(files):
    

    global f
    f=files
    

    
    ans = sorted(files,key=cmp_to_key(myCompare))
    
    return ans
    

    

