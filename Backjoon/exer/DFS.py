import sys
sys.stdin = open("DFS.txt")


def DFS(start):
    print(start, end=' ')
    visited[start] = 1
    for next in range(1, 8):
        if edges[start][next] and not visited[next]:
            DFS(next)


arr = []
for _ in range(8):
    arr.append(list(map(int, input().split())))

visited = [0] * 8
edges = [[0] * 8 for _ in range(8)]


for i in range(len(arr)):
    edges[arr[i][0]][arr[i][1]] = 1
    edges[arr[i][1]][arr[i][0]] = 1

DFS(1)


