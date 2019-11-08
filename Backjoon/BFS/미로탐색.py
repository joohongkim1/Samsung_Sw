import sys
sys.stdin = open("미로탐색.txt")


def is_safe(y, x):
    return 0 <= y < N and 0 <= x < M and arr[y][x] == 1


def BFS(y, x):
    global result
    queue.append([y, x])
    visited[y][x] = 1

    while queue:
        y, x = queue.pop(0)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if is_safe(ny, nx) and not visited[ny][nx]:
                queue.append([ny, nx])
                visited[ny][nx] = 1
                distance[ny][nx] = distance[y][x] + 1
                if ny == N - 1  and nx == M - 1:
                    result = distance[ny][nx] + 1
                    return


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
distance = [[0] * M for _ in range(N)]
start_y, start_x = 0, 0
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
result = 1
queue = []

BFS(start_y, start_x)
print(result)
