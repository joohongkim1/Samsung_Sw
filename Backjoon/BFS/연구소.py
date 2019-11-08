import sys
import itertools
from copy import deepcopy
from collections import deque
from pprint import pprint
sys.stdin = open("연구소.txt")


def is_safe(y, x):
    return 0 <= y < n and 0 <= x < m and arr[y][x] != 1 and arr[y][x] != 2


def BFS(start):
    queue = deque()
    cnt = len(start)
    virus_size = 9999999

    for i in range(len(start)):
        queue.append(start[i])
        visited[start[i][0]][start[i][1]] = 1
    while queue:
        for _ in range(len(queue)):
            start_y, start_x = queue.popleft()

            for dir in range(4):
                ny = start_y + dy[dir]
                nx = start_x + dx[dir]
                if is_safe(ny, nx) and not visited[ny][nx]:
                    queue.append([ny, nx])
                    visited[ny][nx] = 1
                    arr[ny][nx] = 2
                    cnt += 1
                    if cnt > virus_size:
                        return

    if virus_size > cnt:
        virus_size = cnt

    return n * m - cnt_1 - virus_size


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
t_arr = deepcopy(arr)
permu = []
start = []
max_size = 0
cnt_1 = 3
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
for y in range(n):
    for x in range(m):
        if arr[y][x] == 0:
            permu.append([y, x])
        elif arr[y][x] == 2:
            start.append([y, x])
        else:
            cnt_1 += 1

loc = list(itertools.permutations(permu, 3))

for i in range(len(loc)):
    arr = deepcopy(t_arr)
    visited = [[0] * m for _ in range(n)]
    for j in range(3):
        arr[loc[i][j][0]][loc[i][j][1]] = 1

    result = BFS(start)
    if max_size < result:
        max_size = result

print(max_size)
