import sys
from collections import deque
sys.stdin = open("빙산.txt")


def is_safe(y, x):
    return 0 <= y < N and 0 <= x < M and (arr[y][x] != 0)


def check(y, x):
    c = 0
    if arr[y-1][x] == 0:
        c += 1
    if arr[y+1][x] == 0:
        c += 1
    if arr[y][x-1] == 0:
        c += 1
    if arr[y][x+1] == 0:
        c += 1
    return c


def BFS(y, x):
    queue = deque()
    queue.append([y, x])
    visited[y][x] = 1
    while queue:
        y, x = queue.popleft()
        for dir in range(4):
            ny = y + dy[dir]
            nx = x + dx[dir]
            if is_safe(ny, nx) and not visited[ny][nx]:
                queue.append([ny, nx])
                visited[ny][nx] = 1


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
t_arr = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]
cnt = 0
year = 0
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for i in range(N):
    for j in range(M):
        t_arr[i][j] = arr[i][j]

while cnt < 2:
    zero_cnt = 0
    year += 1
    visited = [[0] * M for _ in range(N)]
    cnt = 0
    for y in range(N):
        for x in range(M):
            if arr[y][x] != 0:
                t_arr[y][x] -= check(y, x)
                if t_arr[y][x] < 0:
                    t_arr[y][x] = 0

    for i in range(N):
        for j in range(M):
            arr[i][j] = t_arr[i][j]

    for y in range(N):
        for x in range(M):
            if arr[y][x] != 0 and not visited[y][x]:
                start_y, start_x = y, x
                BFS(y, x)
                cnt += 1
    if cnt >= 2:
        print(year)
        break

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                zero_cnt += 1

    if zero_cnt == N * M:
        print(0)
        break
