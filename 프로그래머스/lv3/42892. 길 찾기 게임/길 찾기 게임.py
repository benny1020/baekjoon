"""
트리를 구성하는 모든 노드 x, y
모든 노드는 서로 다른 x값을 가진다.
같은 level에 있는 노드는 같은 y좌표를 가진다.
자식 노드의 y 값은 항상 부모노드보다 작다
임의의 노드 V의 왼쪽 서브트리에 있는 모든 노드의 x 값은 V의 x 값보다 작다.

전위 순회, 후위순회한 결과를 반환

부모노드를 체크하는게 중요할듯 
"""
import sys
sys.setrecursionlimit(1006)
global back
global front
def frontSearch(cur, childNode):
    global front
    if cur <= -1 or cur > len(childNode):
        return
    front.append(cur+1)
    frontSearch(childNode[cur][0], childNode)
    frontSearch(childNode[cur][1], childNode)
    
def backSearch(cur, childNode):
    global back
    if cur <= -1 or cur > len(childNode):
        return
    backSearch(childNode[cur][0], childNode)
    backSearch(childNode[cur][1], childNode) 
    back.append(cur+1)
    
import copy
def solution(nodeinfo):
    global back
    back = []
    global front
    front = []
    nodeinfoSorted = copy.deepcopy(nodeinfo)

    for i in range(len(nodeinfo)):
        nodeinfoSorted[i].insert(0,i)

    childNode = [[-1,-1] for i in range(len(nodeinfoSorted)+1)] # -1 -> 비었음

    nodeinfoSorted = sorted(nodeinfoSorted, key = lambda x : x[2], reverse = True)
    

    rootNode = nodeinfoSorted[0][0]

    for i in range(len(nodeinfoSorted)-1):
        cur = rootNode
        targetNode = nodeinfoSorted[i+1][0]
        while True:
            if nodeinfo[cur][0] > nodeinfo[targetNode][0]:
                if childNode[cur][0] == -1:
                    childNode[cur][0] = targetNode
                    #print(cur+1, targetNode+1,"left")
                    break
                cur = childNode[cur][0] # 왼쪽
            if nodeinfo[cur][0] < nodeinfo[targetNode][0]:
                if childNode[cur][1] == -1:
                    childNode[cur][1] = targetNode
                    #print(cur+1, targetNode+1,"right")
                    break
                cur = childNode[cur][1] # 오른쪽

    backSearch(rootNode,childNode)
    frontSearch(rootNode,childNode)
    return [front, back]

    
