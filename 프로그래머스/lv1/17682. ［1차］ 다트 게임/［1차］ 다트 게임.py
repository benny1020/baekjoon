def solution(dartResult):
    total = 0
    prev_num = 0
    num = 0

    i=0
    while i<len(dartResult):
        #print(num)
        if dartResult[i]=='1' and i+1<len(dartResult) and dartResult[i+1] =='0'  :
            if num != False:
                total+=num
                num = False
            num = 10

            i+=1
        elif dartResult[i]>='0' and dartResult[i]<= '9':
            if num != False:
                total+=num
                prev_num  = num
                num = False
            num = int(dartResult[i])

        elif dartResult[i] == 'S':
            num = num

        elif dartResult[i] == 'D':
            num = num**2

        elif dartResult[i] == 'T':
            num = num**3

        elif dartResult[i] == '*':
            num = num*2
            total += num
            total += prev_num

            prev_num = num
            num = False

        elif dartResult[i] == '#':
            num = num*(-1)
            total += num
            #total -= prev_num
            prev_num = num
            num = False



        else:
            return -111
        i+=1

    if num != False:
        total += num
    return total