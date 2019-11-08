import sys
from collections import deque
sys.stdin = open("보물섬.txt")


def is_safe(y, x):
    return 0 <= y < N and 0 <= x < M and arr[y][x] == 'L'


def BFS(y, x):
    global result
    queue = deque()
    queue.append([y, x, 0])
    visited[y][x] = 1
    while queue:
        y, x, distance = queue.popleft()
        for dir in range(4):
            ny = y + dy[dir]
            nx = x + dx[dir]
            if is_safe(ny, nx) and not visited[ny][nx]:
                queue.append([ny, nx, distance + 1])
                visited[ny][nx] = 1
                result = max(result, distance)
    return result


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
result = 0
for y in range(N):
    for x in range(M):
        if arr[y][x] == 'L':
            visited = [[0] * M for _ in range(N)]
            BFS(y, x)

print(result + 1)