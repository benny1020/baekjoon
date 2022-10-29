"""
어피치 n발 라이언 n발
어피치 k점 a발 
라이언 k점 b발  더 많이 맞춘 사람이 k점 들고감 같으면 어피치가 가져감
어피치가 이미 솜
라이언이 가장 큰 점수로 우승하기위해 어떻게 점수 내야되는지
지면 -1
"""
global max_score
global max_lion
max_score = -1
max_lion = [0 for i in range(11)]


def search(n, cur, info, lion):
    global max_score
    global max_lion

    # 종료 조건
    if n == 0 or cur == len(info):
        peach_score = 0
        lion_score = 0
        # 점수 계산하기
        for i in range(len(info)):
            if info[i] >= lion[i]:
                if info[i] == 0 and lion[i] == 0:
                    lion_score += (10-i)
                peach_score += (10 - i)
            else:
                lion_score += (10 - i)

        if lion_score - peach_score > max_score:
            max_score = lion_score - peach_score
            max_lion = lion.copy()
            
        if lion_score - peach_score == max_score:
            for i in reversed(range(len(info))):
                if max_lion[i] < lion[i]:
                    max_lion = lion.copy()
                    max_score = lion_score - peach_score
                    return
                elif max_lion[i] > lion[i]:
                    return
                else:
                    continue
        return

    # 라이언이 이김
    if info[cur] + 1 <= n:
        lion[cur] = info[cur] + 1
        search(n - lion[cur], cur + 1, info, lion)
    else:
        lion[cur] = n
        search(0, cur + 1, info, lion)
    # 피치가 이김
    lion[cur] = 0
    search(n, cur + 1, info, lion)
    return


def solution(n, info):
    lion = [0 for i in range(11)]
    search(n, 0, info, lion)
    global max_score
    global max_lion

    if max_score == -1 or max_score == 0:
        return [-1]
    else:
        return max_lion   
    