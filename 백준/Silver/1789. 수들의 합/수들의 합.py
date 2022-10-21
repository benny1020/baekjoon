if __name__ == "__main__":
    n = int(input())
    c = 1
    c_sum = 0
    while c_sum <= n:
        c_sum += c
        c += 1

    print(c-2)