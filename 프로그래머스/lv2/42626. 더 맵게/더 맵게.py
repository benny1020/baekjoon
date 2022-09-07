import heapq
def solution(scoville, K):
    li = [2,1]
    heapq.heapify(scoville)
    num=0
    while(scoville[0] < K):
        if len(scoville) < 2:
            return -1
        heapq.heappush(scoville,heapq.heappop(scoville)+heapq.heappop(scoville)*2)
        num+=1
    return num
    
        
        
    
    