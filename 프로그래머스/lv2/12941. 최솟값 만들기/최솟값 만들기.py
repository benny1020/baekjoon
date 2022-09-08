def solution(A,B):
    answer = 0
    A.sort(reverse=True)
    B.sort()
    total = 0
    for i in range(len(A)):
        total += A[i]*B[i]
    
    return total