import sys
sys.stdin = open("적록색약.txt")


def is_safe(y, x):
    return 0 <= y < N and 0 <= x < N


def BFS(y, x, arr1):
    queue = []
    queue.append([y, x])
    visited[y][x] = 1

    while queue:
        y, x = queue.pop(0)

        for dir in range(4):
            ny = y + dy[dir]
            nx = x + dx[dir]
            if is_safe(ny, nx) and not visited[ny][nx] and arr1[ny][nx] == arr1[y][x]:
                queue.append([ny, nx])
                visited[ny][nx] = 1


N = int(input())
arr = [list(input()) for _ in range(N)]
t_arr = [[''] * N for _ in range(N)]
visited = [[0] * N for _ in range(N)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
cnt = 0
cnt2 = 0
for i in range(N):
    for j in range(N):
        t_arr[i][j] = arr[i][j]
        if arr[i][j] == 'G':
            arr[i][j] = 'R'


for y in range(N):
    for x in range(N):
        if not visited[y][x]:
            start_y, start_x = y, x
            BFS(start_y, start_x, arr)
            cnt += 1

visited = [[0] * N for _ in range(N)]
for y in range(N):
    for x in range(N):
        if not visited[y][x]:
            start_y, start_x = y, x
            BFS(start_y, start_x, t_arr)
            cnt2 += 1

print(cnt2, cnt)