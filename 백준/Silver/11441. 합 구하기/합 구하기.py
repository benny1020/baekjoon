import sys
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    for i in range(1, len(arr)):
        arr[i] += arr[i - 1]
    m = int(sys.stdin.readline().rstrip())
    for i in range(m):
        a, b = map(int, sys.stdin.readline().rstrip().split(' '))
        if a-2 >= 0:
            print(arr[b-1] - arr[a-2])
        else:
            print(arr[b-1])