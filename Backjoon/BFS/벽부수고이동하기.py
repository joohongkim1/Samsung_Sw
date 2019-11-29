import sys
from collections import deque
sys.stdin = open("벽부수고이동하기.txt")


def is_safe(y, x):
    return 0 <= y < N and 0 <= x < M and (arr[y][x] == 0)


def BFS(y, x):
    global min_var
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
                visited[ny][nx] = visited[y][x] + 1
                if ny == N - 1 and nx == M - 1:
                    if visited[ny][nx] < min_var:
                        min_var = visited[ny][nx]


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
visited2 = [[0] * M for _ in range(N)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
result = []
min_var = 999999
if arr[0][1] and arr[0][2] and arr[1][0] and arr[1][1] and arr[2][0]:
    print(-1)
elif arr[N - 1][M - 1] and arr[N - 2][M - 1] and arr[N - 3][M - 1] and arr[N - 2][M - 2] and arr[N - 1][M - 2] and arr[N - 1][M - 3]:
    print(-1)
else:
    for y in range(N):
        for x in range(M):
            if visited2[y][x] == 0:
                if arr[y][x] == 1:
                    arr[y][x] = 0
                    visited2[y][x] = 1
                    BFS(0, 0)
                    arr[y][x] = 1

    if min_var == 0:
        print(-1)
    print(min_var)
