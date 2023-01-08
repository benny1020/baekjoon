import copy 
            
# 2,2 -> 0,2
# 0,1 -> 1,0
def getKeyRotation(key):
    rotationKey = [[] for i in range(len(key))]
    
    for i in range(len(key)):
        rotationKey[i] = [key[j][i] for j in reversed(range(len(key)))]
    return rotationKey


def solution(key, lock):
    newLockLength = len(lock) + (len(key) - 1) * 2
    newLock = [[1 for i in range(newLockLength)] for j in range(newLockLength)]
    for i in range(len(lock)):
        for j in range(len(lock)):
            newLock[i+(len(key)-1)][j+(len(key)-1)] = lock[i][j]
    
    newLockArray = []
    cnt = 0
    for i in range(len(newLock)):
        for j in range(len(newLock)):
            if newLock[i][j] == 0:
                cnt+=1
                newLockArray.append(i*len(newLock)+j)
    if cnt == 0:
        return True
    for i in range(4):
        key = getKeyRotation(key)
        for i in range(len(newLock)-len(key)+1):
            for j in range(len(newLock)-len(key)+1):
                c = 0
                flag = True
                for a in range(len(key)):
                    for b in range(len(key)):
                        if key[a][b] == 1:
                            if newLock[a+i][b+j] == 0:
                                c += 1
                            if newLock[a+i][b+j] == 1:
                                if len(key) - 2 < a+i < len(key)-2 + len(lock) and len(key) - 2 < b+j < len(key)-2 + len(lock) :
                                    flag = False
                                    break
                                    
                    if flag == False:
                        break
                if c == cnt:
                    return True
    return False
                
                        
        