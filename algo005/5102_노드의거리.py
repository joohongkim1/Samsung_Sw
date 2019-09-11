import sys
sys.stdin = open("5102_input.txt")


def BFS(start_node):
    global result
    queue.append(start_node)
    visited[start_node] = 1

    while queue:
        start_node = queue.pop(0)
        for next_node in range(1, v+1):
            if my_map[start_node][next_node] and not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = 1
                distance[next_node] = distance[start_node] + 1
                if next_node == end_node:
                    result = distance[next_node]
                    return
    return


TC = int(input())
for tc in range(1, TC+1):
    v, e = map(int, input().split())
    my_map = [[0] * (v+1) for _ in range(v+1)]
    distance = [0] * (v + 1)
    visited = [0] * (v + 1)
    result = 0
    for i in range(e):
        start, end = map(int, input().split())
        my_map[start][end] = 1
        my_map[end][start] = 1
    start_node, end_node = map(int, input().split())
    queue = []
    BFS(start_node)
    print('#{} {}'.format(tc, result))

