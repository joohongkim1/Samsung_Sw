import sys
sys.stdin = open("미로의거리.txt")


def is_safe(y, x):
    return 0 <= y < N and 0 <= x < N and (maze[y][x] == 0 or maze[y][x] == 3)


def BFS(y, x):
    global result
    queue.append((y, x))
    visited[y][x] = 1

    while queue:
        y, x = queue.pop(0)
        for i in range(4):
            new_y = y + dy[i]
            new_x = x + dx[i]
            if is_safe(new_y, new_x) and not visited[new_y][new_x]:
                queue.append([new_y, new_x])
                visited[new_y][new_x] = 1
                distance[new_y][new_x] = distance[y][x] + 1
                if maze[new_y][new_x] == 3:
                    result = distance[new_y][new_x] - 1
                    return


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    distance = [[0] * N for _ in range(N)]
    result = 0
    queue = []
    for y in range(N):
        for x in range(N):
            if maze[y][x] == 2:
                start_y, start_x = y, x

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    BFS(start_y, start_x)
    print('#{} {}'.format(tc, result))


