if __name__ == "__main__":
    n, x = map(int, input().split())

    visits = list(map(int, input().split()))
    maxx = 0
    count = dict()
    tmp = 0
    for i in range(n-x+1):
        if i != 0 :
            tmp -= visits[i-1]
            tmp += visits[i+x-1]
        else:
            tmp = sum(visits[i:i+x])
        if tmp > maxx:
            maxx = tmp
        if tmp not in count:
            count[tmp] = 1
        else:
            count[tmp] += 1

    if maxx == 0:
        print("SAD")
    else:
        print(maxx)
        print(count[maxx])
