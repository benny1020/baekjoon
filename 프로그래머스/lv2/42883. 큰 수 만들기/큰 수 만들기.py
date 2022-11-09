"""
len(number) - k만큼 뽑으면 된다?
1 9 2 4 


1 
1 9 2

더뽑아야 할때
3234

딱맞을대
477
"""
def solution(number, k):

    answer = [number[0]]
    for i in range(1, len(number)):
        while len(answer) > 0 and answer[-1] < number[i]:
            if (len(number) - i) == len(number) - k - len(answer):
                break
            answer.pop()
        if len(answer) < len(number)-k: 
            answer.append(number[i])
            
    return ''.join(answer)
            
            
        
    return answer