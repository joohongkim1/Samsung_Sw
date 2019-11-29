import sys
from pprint import pprint
sys.stdin = open("7465_input.txt", "r")


def DFS(v):
    print(v)
    result.append(v)
    visited[v] = True

    for x in range(1, N+1):
        if G[v][x] and not visited[x]:
            DFS(x)


TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    arr = []
    result = []
    visited = [0] * (N + 1)
    for m in range(M):
        arr.append(list(map(int, input().split())))

    G = [[0] * (N+1) for _ in range(N+1)]

    for i in range(len(arr)):
        G[arr[i][0]][arr[i][1]] = 1
        G[arr[i][1]][arr[i][0]] = 1

    DFS(arr[0][0])

