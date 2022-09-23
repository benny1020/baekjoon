
if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        num = int(input())
        li = list(map(int, input().split(' ')))
        print(str(min(li))+' '+str(max(li)))
