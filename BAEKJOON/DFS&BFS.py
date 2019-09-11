import sys
sys.stdin = open("input.txt")

def DFS(v):
    visited = [0] * (N+1)
    stack = [0] * 10
    top = 0
    stack[top] = v
    while top != -1:
        v = stack[top]
        top -= 1
        if visited[v] != 1:
            visited[v] = 1
            print(v, end=' ')
            for i in range(N, 1, -1):
                if my_map[v][i] and not visited[i]:
                    top += 1
                    stack[top] = i

def BFS(start_node):
    queue = []
    visited = [0] * (N+1)
    queue.append(start_node)
    visited[start_node] = 1

    while queue:
        start_node = queue.pop(0)
        print(start_node, end=' ')
        for next_node in range(1, N+1):
            if my_map[start_node][next_node] and not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = 1


N, M, start_node = map(int, input().split())
my_map = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(M):
    start, end = map(int, input().split())
    my_map[start][end] = 1
    my_map[end][start] = 1
DFS(start_node)
print()
BFS(start_node)