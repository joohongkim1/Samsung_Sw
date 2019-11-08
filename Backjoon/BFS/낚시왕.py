import sys
from pprint import pprint
sys.stdin = open("낚시왕.txt")


r, c, m = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(m)]
arr = [[0] * c for _ in range(r)]
idx = -1
fish = 0
for i in range(m):
    arr[info[i][0] - 1][info[i][1] - 1] = info[i][2:5]
pprint(arr)
# 이동방향 :  s는 속력, d는 이동 방향, z는 크기이다.
# d가 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽을 의미한다.
while idx < c:
    idx += 1

    for row in range(r):
        if arr[row][idx] != 0:
            fish += arr[row][idx][2]
            arr[row][idx] = 0
            break

    for y in range(r):
        for x in range(c):
            if arr[y][x] != 0:
                if arr[y][x][1] == 1:
                    if y - arr[y][x][0] >= 0:
                        arr[y - arr[y][x][0]][x] = arr[y][x]
