import sys
sys.stdin = open("view.txt")


for tc in range(1, 11):
    length = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    for i in range(2, length-2):
        result = arr[i] - max(arr[i-2], arr[i-1], arr[i+1], arr[i+2])
        if result >= 1:
            cnt += result

    print('#{} {}'.format(tc, cnt))




