import sys
from pprint import pprint
sys.stdin = open("촌수계산.txt")


def BFS(x):
    global result
    queue = []
    queue.append(x)
    visited[x] = 1
    while queue:
        x = queue.pop(0)
        for i in range(1, n+1):
            if linked_arr[x][i] and not visited[i]:
                queue.append(i)
                visited[i] = 1
                distance[i] = distance[x] + 1
                if i == start_x:
                    result = distance[i]
                    return


n = int(input())
start_x, start_y = map(int, input().split())
m = int(input())
linked_arr = [[0] * (n+1) for _ in range(n+1)]
visited = [0] * (n+1)
distance = [0] * (n+1)
result = 0

for _ in range(m):
    a, b = map(int, input().split())
    linked_arr[a][b] = 1
    linked_arr[b][a] = 1

BFS(start_y)
if not result:
    print(-1)
else:
    print(result)

