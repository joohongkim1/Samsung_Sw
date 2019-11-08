import sys
sys.stdin = open("미로.txt")


def is_Safe(y, x):
    return 0<= y < N and 0 <= x < N and (maze[y][x] == 0 or maze[y][x] == 3)


def DFS(y, x):
    global result
    visited[y][x] = 1
    if maze[y][x] == 3:
        result = 1
        return

    for i in range(4):
        new_y = y + dy[i]
        new_x = x + dx[i]
        if is_Safe(new_y, new_x) and not visited[new_y][new_x]:
            DFS(new_y, new_x)


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    result = 0

    for y in range(N):
        for x in range(N):
            if maze[y][x] == 2:
                start_y, start_x = y, x

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    DFS(start_y, start_x)
    print('#{} {}'.format(tc, result))