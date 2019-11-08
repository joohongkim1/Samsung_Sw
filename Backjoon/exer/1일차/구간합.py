import sys
sys.stdin = open("구간합_input.txt")


TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    max_sum = 0
    min_sum = 10000000
    for i in range(N-M+1):
        sum_var = 0
        for j in range(i, i+M):
            sum_var += arr[j]
        if max_sum < sum_var:
            max_sum = sum_var
        if min_sum > sum_var:
            min_sum = sum_var

    print('#{} {}'.format(tc, max_sum - min_sum))