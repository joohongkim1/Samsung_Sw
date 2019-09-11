import sys
sys.stdin = open("단어_input.txt")


TC = int(input())
for tc in range(1, TC+1):
    N, K = map(int, input().split())
    puzzle = [[0] * N for _ in range(N)]
    result = 0
    count_row = 0
    count_col = 0

    for i in range(N):
        puzzle[i] = list(map(int, input().split()))

    for i in range(N):
        if count_row == K:
            result += 1
        count_row = 0
        for j in range(N):
            if puzzle[i][j] == 1:
                count_row += 1
            else:
                if count_row == K:
                    result += 1
                count_row = 0
    if count_row == K:
        result += 1

    for i in range(N):
        if count_col == K:
            result += 1
        count_col = 0
        for j in range(N):
            if puzzle[j][i] == 1:
                count_col += 1
            else:
                if count_col == K:
                    result += 1
                count_col = 0
    if count_col == K:
        result += 1
    print('#{} {}'.format(tc, result))