import sys
from pprint import pprint
sys.stdin = open("안전영역.txt")



def is_safe(y, x):
    return 0 <= y < N and 0 <= x < N and (arr[y][x] != 0)


def BFS(y, x):
    queue = []
    queue.append([y, x])
    visited[y][x] = 1

    while queue:
        y, x = queue.pop(0)
        for dir in range(4):
            ny = y + dy[dir]
            nx = x + dx[dir]
            if is_safe(ny, nx) and not visited[ny][nx]:
                queue.append([ny, nx])
                visited[ny][nx] = 1


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
max_var = 0
for i in range(N):
    for j in range(N):
        if max_var < arr[i][j]:
            max_var = arr[i][j]
max_cnt = 0
rain = -1

while rain <= max_var:
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    rain += 1
    for a in range(N):
        for b in range(N):
            if arr[a][b] <= rain:
                arr[a][b] = 0
    for y in range(N):
        for x in range(N):
            if arr[y][x] != 0 and not visited[y][x]:
                start_y, start_x = y, x
                BFS(start_y, start_x)
                cnt += 1
    if max_cnt < cnt:
        max_cnt = cnt

print(max_cnt)