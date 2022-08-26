def getArray(n,arr):
    array = []
    
    for num in arr:
        s =  ""
        for i in range(n):
            if num >= 2**(n-i-1):
                s+='#'
                num = num - 2**(n-i-1)
            else:
                s+=' '
        array.append(s)
    return array

            

def solution(n, arr1, arr2):
    array1 = getArray(n,arr1)
    array2 = getArray(n,arr2)
    for i in range(n):
        for j in range(n):
            if array2[i][j] =='#':
                li = list(array1[i])
                li[j]='#'
                array1[i] = ''.join(li)
    return  array1