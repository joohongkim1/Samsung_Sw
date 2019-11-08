import sys
sys.stdin = open("특별한정렬_input.txt")


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr = sorted(arr)
    print('#{}'.format(tc), end=' ')
    for k in range(5):
        print('{} {}'.format(arr[-k-1], arr[k]), end=' ')
    print()


