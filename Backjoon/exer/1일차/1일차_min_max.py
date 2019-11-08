import sys
sys.stdin = open("min_max_input.txt")


TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_var = 0
    min_var = 100000000

    for i in arr:
        if i < min_var:
            min_var = i
        if i > max_var:
            max_var = i

    print('#{} {}'.format(tc, max_var - min_var))