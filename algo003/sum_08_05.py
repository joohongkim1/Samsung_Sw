import sys
sys.stdin = open("sum_input.txt")


for tc in range(1, 11):
    n = int(input())
    my_map = [list(map(int, input().split())) for _ in range(100)]
    max_val = 0
    sum_x1 = 0
    sum_x2 = 0

    for i in range(100):  # 각 행, 열의 합 구한 후 최대값 업데이트
        sum_col = 0
        if max_val < sum(my_map[i]):
            max_val = sum(my_map[i])
        for j in range(100):
            sum_col += my_map[j][i]
        if max_val < sum_col:
            max_val = sum_col

    for i in range(100):
        sum_x1 += my_map[i][i]
        if max_val < sum_x1:
            max_val = sum_x1

    for i in range(100):
        sum_x2 += my_map[i][100-i-1]
        if max_val < sum_x2:
            max_val = sum_x2

    print('#{} {}'.format(tc, max_val))
