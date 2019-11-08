import sys
sys.stdin = open("경로찾기.txt")


for tc in range(1, 3):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for k in range(0, N):
        for i in range(0, N):
            for j in range(0, N):
                if arr[i][k] and arr[k][j]:
                    arr[i][j] = 1

    for x in range(len(arr)):
        for y in range(len(arr)):
            print(arr[x][y], end=' ')
        print()