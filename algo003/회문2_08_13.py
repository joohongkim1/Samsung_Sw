import sys
sys.stdin = open("회문2_input.txt")


for tc in range(1, 11):
    n = int(input())
    a = [''] * 8
    count = 0
    max_val = 0
    result = True

    for i in range(8):
        a[i] = input()

    for i in range(8):
        for j in range(9-n):
            result = True
            for k in range(n//2):
                if a[i][j+k] != a[i][j+n-k-1]:
                    result = False
                    break
            if result:
                count += 1

    for i in range(8):
        for j in range(9-n):
            result = True
            for k in range(n//2):
                if a[j + k][i] != a[j+n-k-1][i]:
                    result = False
                    break
            if result:
                count += 1
    print('#{} {}'.format(tc, count))