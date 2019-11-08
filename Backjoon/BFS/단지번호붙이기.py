import sys
from pprint import pprint
sys.stdin = open("단지번호붙이기.txt")


def is_safe(y, x):
    return 0 <= y < N and 0 <= x < N and arr[y][x] == 1


def BFS(y, x):
    global cnt
    queue = []
    queue.append([y, x])
    visited[y][x] = 1
    arr[y][x] = cnt + 1
    cnt += 1
    while queue:
        y, x = queue.pop(0)

        for dir in range(4):
            ny = y + dy[dir]
            nx = x + dx[dir]

            if is_safe(ny, nx) and not visited[ny][nx]:
                queue.append([ny, nx])
                visited[ny][nx] = 1
                arr[ny][nx] = cnt


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
temp_arr = [[0] * N for _ in range(N)]
visited = [[0] * N for _ in range(N)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
cnt = 0
cnt_danji = []

for y in range(N):
    for x in range(N):
        if arr[y][x] == 1:
            if visited[y][x] == 1:
                continue
            else:
                start_y, start_x = y, x
                BFS(start_y, start_x)

for i in range(N):
    for j in range(N):
        if arr[i][j] not in cnt_danji and arr[i][j] != 0:
            cnt_danji.append(arr[i][j])

cnt_arr = [0] * len(cnt_danji)

for a in range(N):
    for b in range(N):
        for c in range(len(cnt_danji)):
            if arr[a][b] == cnt_danji[c]:
                cnt_arr[c] += 1

cnt_arr.sort()
print(len(cnt_arr))

for z in range(len(cnt_arr)):
    print(cnt_arr[z])