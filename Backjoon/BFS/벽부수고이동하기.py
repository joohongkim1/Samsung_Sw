import sys
sys.stdin = open("벽부수고이동하기.txt")


def is_safe(y, x):
    return 0 <= y < N and 0 <= x < M and not arr[y][x]


def BFS(y, x):
    global flag
    global result
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
                distance[ny][nx] = distance[y][x] + 1
                if ny == N-1 and nx == M-1:
                    flag = True
                    result = distance[ny][nx] + 1


def BFS2(y, x, d):
    global flag2
    global result2
    queue = []
    queue.append([y, x, d])
    visited[y][x] = 1
    while queue:
        y, x, d = queue.pop(0)
        for dir in range(4):
            ny = y + dy[dir]
            nx = x + dx[dir]
            if is_safe(ny, nx) and not visited[ny][nx]:
                queue.append([ny, nx, d+1])
                visited[ny][nx] = 1
                if ny == N-1 and nx == M-1:
                    flag2 = True
                    result2 = d + 2


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
distance = [[0] * M for _ in range(N)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
min_val = 999999
flag = False
flag2 = False
result = 0
result2 = 0
BFS(0, 0)
if flag:
    if min_val > result:
        min_val = result

for y in range(N):
    for x in range(M):
        flag2 = False
        result2 = 0
        visited = [[0] * M for _ in range(N)]
        if arr[y][x] == 1:
            arr[y][x] = 0
            BFS2(0, 0, 0)
            arr[y][x] = 1
            if flag and flag2:
                if result > result2:
                    min_val = result2
            elif flag2:
                min_val = result2

if min_val == 999999:
    print(-1)
else:
    print(min_val)
