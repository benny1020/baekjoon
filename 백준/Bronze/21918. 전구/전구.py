
if __name__ == "__main__":
    n, m = map(int, input().split(' '))

    light = list(map(int, input().split(' ')))

    for i in range(m):
        a, b, c = map(int, input().split(' '))
        if a == 1:
            light[b-1] = c
        elif a == 2:
            for j in range(b-1, c):
                if light[j] == 0:
                    light[j] = 1
                else:
                    light[j] = 0

        elif a == 3:
            for j in range(b-1, c):
                light[j] = 0
        # a== 4
        else:
            for j in range(b-1, c):
                light[j] = 1

    for l in light:
        print(l, end=' ')

