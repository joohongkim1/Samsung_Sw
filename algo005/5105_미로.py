import sys
sys.stdin = open("5105_input.txt")


def isWall(y, x):
    return 0 <= y < n and 0 <= x < n and (maze[y][x] == 0 or maze[y][x] == 3)


def BFS(start_y, start_x):
    global result
    queue.append((start_y, start_x))
    visited.append((start_y, start_x))

    while queue:
        start_y, start_x = queue.pop(0)

        for dir in range(4):
            newX = start_x + dx[dir]
            newY = start_y + dy[dir]
            if isWall(newY, newX) and (newY, newX) not in visited:
                queue.append((newY, newX))
                visited.append((newY, newX))
                distance[newY][newX] = distance[start_y][start_x] + 1
                if maze[newY][newX] == 3:
                    result = distance[newY][newX] - 1
                    return


TC = int(input())
for tc in range(1, TC+1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]
    visited = []
    distance = [[0] * n for _ in range(n)]
    queue = []
    result = 0
    for y in range(n):
        for x in range(n):
            if maze[y][x] == 2:
                start_y, start_x = y, x

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    BFS(start_y, start_x)
    print('#{} {}'.format(tc, result))
