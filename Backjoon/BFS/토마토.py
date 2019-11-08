from collections import deque


def is_safe(y, x):
    return 0 <= y < n and 0 <= x < m and not arr[y][x]


def BFS(start):
    for i in range(len(start)):
        queue.append(start[i])

    while queue:
        global result
        for j in range(len(queue)):
            y, x = queue.popleft()
            for dir in range(4):
                ny = y + dy[dir]
                nx = x + dx[dir]
                if is_safe(ny, nx) and not arr[ny][nx]:
                    queue.append([ny, nx])
                    arr[ny][nx] = 1
                    distance[ny][nx] = distance[y][x] + 1
                    result = distance[ny][nx]


m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            cnt += 1
if not cnt:
    print(0)
else:

    distance = [[0] * m for _ in range(n)]
    queue = deque()
    start = []
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    cnt = 0

    for y in range(n):
        for x in range(m):
            if arr[y][x] == 1:
                start.append([y, x])

    BFS(start)
    for a in range(n):
        for b in range(m):
            if arr[a][b] == 0:
                cnt += 1
                break
    if cnt == 0:
        print(result)
    else:
        print(-1)