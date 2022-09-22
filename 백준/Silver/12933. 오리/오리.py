"""
q a u a c k c k

q u a c k
q u a c k
q u a c k
"""

if __name__ == "__main__":

    quack = ['q', 'u', 'a', 'c', 'k']
    ans = 0
    s = input()

    quack_list = []

    for q in s:
        if q == 'q':
            if ans > 0:
                ans -= 1
            quack_list.append(['q'])
            continue
        else:
            if len(quack_list) == 0:
                print(-1)
                exit(0)
        for i in range(len(quack_list)):
            if quack[len(quack_list[i])] == q:
                quack_list[i].append(q)
                if q == 'k':
                    quack_list.pop(i)
                    ans += 1
                break
            if i == len(quack_list)-1:
                print(-1)
                exit(0)

    if len(quack_list) != 0:
        print(-1)
        exit(0)
    print(ans)


