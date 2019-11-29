import sys
from collections import deque
sys.stdin = open("숨바꼭질.txt")


def is_safe(x):
    return 0 <= x < max


def BFS(x):
    queue = deque()
    queue.append(x)
    while queue:
        x = queue.popleft()
        dx = [-1, 1, 2 * x]
        for i in range(3):
            if i != 3:
                nx = x + dx[i]
            else:
                nx = dx[i]

            if is_safe(nx) and not visited[nx]:
                queue.append(nx)
                visited[nx] = 1
                distance[nx] = distance[x] + 1
                if nx == y:
                    return


x, y = map(int, input().split())
max = y * 2
arr = [0] * max
visited = [0] * max
distance = [0] * max

BFS(x)
print(distance[y] + 1)
