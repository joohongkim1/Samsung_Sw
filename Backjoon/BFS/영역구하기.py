import sys
from pprint import pprint
sys.stdin = open("영역구하기.txt")


def is_safe(y, x):
    return 0 <= y < M and 0 <= x < N and (arr[y][x] != 0)


def BFS(y, x):
    global count
    global cnt
    queue = []
    queue.append([y, x])
    visited[y][x] = 1
    count = 1
    while queue:
        y, x= queue.pop(0)
        for dir in range(4):
            ny = y + dy[dir]
            nx = x + dx[dir]
            if is_safe(ny, nx) and not visited[ny][nx]:
                queue.append([ny, nx])
                visited[ny][nx] = 1
                count += 1


M, N, K = map(int, input().split())
arr = [[1] * N for _ in range(M)]
cnt = 0
count = 0
result = []
visited = [[0] * N for _ in range(M)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] = 0
for y in range(M):
    for x in range(N):
        if arr[y][x] != 0 and not visited[y][x]:
            BFS(y, x)
            result.append(count)
            cnt += 1
print(cnt)
result.sort()
for i in range(len(result)):
    print(result[i], end=' ')




