import sys
from pprint import pprint
sys.stdin = open("contact_input.txt")


def BFS(start_node):
    queue.append(start_node)
    visited[start_node] = 1
    max_value = 0

    while queue:
        start_node = queue.pop(0)
        for next_node in range(1, max_var):
            if my_map[start_node][next_node] and not visited[next_node]:
                visited[next_node] = 1
                queue.append(next_node)
                distance[next_node] = distance[start_node] + 1
    for j in range(1, max_var):
        if distance[j] >= max_value:
            max_value = distance[j]
    for k in range(max_var-1, 0, -1):
        if distance[k] >= max_value:
            max_value = distance[k]
        if distance[k] == max_value:
            return k

for tc in range(1, 11):
    data_len, start_node = map(int, input().split())
    start_to_end = list(map(int, input().split()))
    max_var = max(start_to_end)
    my_map = [[0] * (max_var + 1) for _ in range(max_var + 1)]
    visited = [0] * (max_var + 1)
    distance = [0] * (max_var + 1)
    for i in range(1, data_len+1):
        if i % 2:
            start = start_to_end[i-1]
            end = start_to_end[i]
            my_map[start][end] = 1
    queue = []
    print('#{} {}'.format(tc, BFS(start_node)))
    

