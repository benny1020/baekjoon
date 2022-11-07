if __name__ == "__main__":
    n, m = map(int, input().split())

    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    answer = []

    a.extend(b)

    a_idx = 0
    b_idx = n

    while not(a_idx >= n and b_idx >= n+m):
        if a_idx == n:
            answer.append(a[b_idx])
            b_idx += 1
            continue
        elif b_idx == n+m:
            answer.append(a[a_idx])
            a_idx += 1
            continue
        if a[a_idx] < a[b_idx]:
            answer.append(a[a_idx])
            a_idx += 1
        else:
            answer.append(a[b_idx])
            b_idx += 1

    for ans in answer:
        print(ans, end=' ')