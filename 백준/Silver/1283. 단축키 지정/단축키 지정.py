num = int(input())
shortcut = []
#print(num)

for k in range(num):
    flag= False
    str = input().split(' ')
    #단어 앞에꺼 모두 확인
    for i in range(len(str)):
        if str[i][0].lower() not in shortcut:
            shortcut.append(str[i][0].lower())
            str[i] = str[i].replace(str[i][0],'['+str[i][0]+']',1)
            flag = True
            break


    #왼쪽부터 차례대로 확인
    if(flag == False):
        for i in range(len(str)):
            if(flag == True):
                break
            for j in range(len(str[i])):
                if str[i][j].lower() not in shortcut:
                    shortcut.append(str[i][j].lower())
                    str[i] = str[i].replace(str[i][j],'['+str[i][j]+']',1)
                    flag = True
                    break

    if flag == False:
        shortcut.append(' ')

    for i in range(len(str)-1):
        print(str[i],end=' ')
    print(str[len(str)-1])