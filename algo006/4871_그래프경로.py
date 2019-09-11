import sys
from pprint import pprint
sys.stdin = open("4871_input.txt")


def DFSr(start_node):
    global result
    visited[start_node] = True
    for i in range(1, v+1):
        if my_map[start_node][i] and not visited[i]:
            if i == end_node:
                result = 1
            else:
                DFSr(i)

# def DFS(start_node):
#     top = 0
#     stack = [0] * v
#     stack[top] = start_node
#     while top != -1:
#         start_node = stack[top]
#         top -= 1
#         if not visited[start_node]:
#             visited[start_node] = 1
#             for i in range(1, v+1):
#                 if my_map[start_node][i] and not visited[i]:
#                     top += 1
#                     stack[top] = i
#                     if stack[top] == end_node:
#                         return 1
#     return 0

TC = int(input())
for tc in range(1, TC+1):
    v, e = map(int, input().split())
    my_map = [[0] * (v+1) for _ in range(v+1)]
    visited = [0] * (v+1)
    result = 0
    for i in range(e):
        start, end = map(int, input().split())
        my_map[start][end] = 1

    start_node, end_node = map(int, input().split())
    DFSr(start_node)
    print('#{} {}'.format(tc, result))