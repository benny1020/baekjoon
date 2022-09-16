"""
2 X N 명의 사원 두팀으로 나누어

승리한 쪽이 1점
같으면 0점

A팀의 출전 순서 공개

B팀이 가장 높은 승점 몇인지

A팀에서 제일 작은 애 한명 뽑는다

B팀에서도 제일 작은애 한명 뽑는다

A < B 이면
score +=1
끝

반대이면 
tmp에 넣고 돌림

끝까지 다돌았는데도 그러면
tmp 0번째 인덱스 빼고 B에 다 넣음

"""
import heapq
def solution(a, b):
    a = [-i for i in a]
    b = [-i for i in b]
    heapq.heapify(a)
    heapq.heapify(b)
    answer = 0
    while b and a:
        am = heapq.heappop(a)
        bm = heapq.heappop(b)
        if -am < -bm:
            answer += 1
        else:
            heapq.heappush(b, bm)
    return answer

