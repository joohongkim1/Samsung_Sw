import sys
sys.stdin = open("나이트이동.txt")


def is_safe(y, x):
    return 0 <= y < N and 0 <= x < N


def BFS(y, x):
    global result
    if y == ty and x == tx:
        return
    queue = []
    queue.append([y, x])
    visited[y][x] = 1

    while queue:
        y, x = queue.pop(0)
        for dir in range(8):
            ny = y + dy[dir]
            nx = x + dx[dir]
            if is_safe(ny, nx) and not visited[ny][nx]:
                queue.append([ny, nx])
                visited[ny][nx] = 1
                distance[ny][nx] = distance[y][x] + 1
                if ny == ty and nx == tx:
                    result = distance[ny][nx]
                    return


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    distance = [[0] * N for _ in range(N)]
    y, x = map(int, input().split())
    ty, tx = map(int, input().split())
    result = 0
    dy = [-2, -1, -2, -1, 1, 2, 2, 1]
    dx = [-1, -2, 1, 2, -2, -1, 1, 2]

    BFS(y, x)
    print(result)

