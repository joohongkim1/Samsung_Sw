import sys
sys.stdin = open("palin_input.txt", "r")


def isPalinH(x, y) :
    for i in range(M//2):
        if s[x][y + i] != s[x][y + (M - 1) - i]:
            return False
    print(s[x][y:y + M])
    return True


def isPalinV(x, y) :
    for i in range(M//2):
        if s[x + i][y] != s[x + (M - 1) - i][y]:
            return False

    for _ in range(x, x + M):
        print(s[_][y], end='')
    print()
    return True


TC = int(input())
for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    s = [input() for i in range(N)]

    print("#%d " % tc, end = '')

    found = False
    for i in range(N):
        if found:
            break
        for j in range(N - M + 1):
            if isPalinH(i, j):
                break
            if isPalinV(j, i):
                break
