import sys
from collections import deque
sys.stdin = open("DFS와BFS.txt")


def DFS(start):
    print(start, end=' ')
    visited[start] = 1

    for next in range(1, N+1):
        if edges[start][next] and not visited[next]:
            DFS(next)


def BFS(start):
    queue = deque()
    queue.append(start)

    while queue:
        start = queue.popleft()
        if start not in visited:
            visited.append(start)
            for next in range(1, N + 1):
                if edges[start][next] and next not in visited:
                    queue.append(next)

    return visited


N, M, V = map(int, input().split())
arr = []

for _ in range(M):
    arr.append(list(map(int, input().split())))

visited = [0] * (N + 1)
edges = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(M):
    edges[arr[i][0]][arr[i][1]] = 1
    edges[arr[i][1]][arr[i][0]] = 1


DFS(V)
visited = []
print()
BFS(V)
for i in range(len(visited)):
    print(visited[i], end=' ')