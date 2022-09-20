"""
N개의 회의를 모두 진행할 수 있는 최소 회의실 개수
"""

from functools import cmp_to_key
import heapq

def myCompare(meeting1, meeting2):
    if meeting1[0] > meeting2[0]:
        return 1
    if meeting1[0] == meeting2[0]:
        if meeting1[1] > meeting2[1]:
            return 1
    return -1

if __name__ == "__main__":

    n = int(input())
    meetings = []
    room = []
    heapq.heapify(room)

    for i in range(n):
        meetings.append(list(map(int,input().split(' '))))

    meetings = sorted(meetings, key=cmp_to_key(myCompare))
    room.append(meetings.pop(0)[1])

    # 제일 작은 미팅 시작시간
    # 가장 작은 끝나는 시간
    for meeting in meetings:
        if meeting[0] < room[0]:
            heapq.heappush(room, meeting[1])
        else:
            heapq.heappop(room)
            heapq.heappush(room, meeting[1])

    print(len(room))

