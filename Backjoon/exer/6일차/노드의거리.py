import sys
sys.stdin = open("노드의거리.txt")


def BFS(start_node):
    global result
    queue.append(start_node)
    visited[start_node] = 1

    while queue:
        start_node = queue.pop(0)
        for next_node in range(1, V+1):
            if arr[start_node][next_node] and not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = 1
                distance[next_node] = distance[start_node] + 1
                if next_node == end_node:
                    result = distance[next_node]


TC = int(input())
for tc in range(1, TC+1):
    V, E = map(int, input().split())
    arr = [[0] * (V+1) for _ in range(V+1)]
    visited = [0] * (V+1)
    distance = [0] * (V+1)
    queue = []
    result = 0

    for i in range(E):
        start, end = map(int, input().split())
        arr[start][end] = 1
        arr[end][start] = 1
    start_node, end_node = map(int, input().split())
    BFS(start_node)
    print('#{} {}'.format(tc, result))




