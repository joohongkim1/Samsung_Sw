import sys
sys.stdin = open("sum.txt")


for tc in range(1, 11):
    TC = int(input())
    arr = [0] * 100
    max_var = 0
    right_dia = 0
    left_dia = 0

    for t in range(100):
        arr[t] = list(map(int, input().split()))

    for i in range(100):
        row_sum = 0
        col_sum = 0
        for j in range(100):
            row_sum += arr[i][j]
            col_sum += arr[j][i]
            result = max(col_sum, row_sum)
        if max_var < result:
            max_var = result

        right_dia += arr[i][i]
        left_dia += arr[i][100-i-1]
    result = max(right_dia, left_dia)

    if max_var < result:
        max_var = result

    print('#{} {}'.format(tc, max_var))



