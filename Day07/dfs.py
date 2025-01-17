# 반복문
def DFS(v):
    visited = [0] * 8
    stack = [0] * 10
    top = 0
    stack[top] = v
    while top != -1:
        v = stack[top]
        top -= 1
        if visited[v] != 1:
            visited[v] = 1
            print(v)
            for i in range(1, 8):
                if G[v][i] and not visited[i]:
                    top += 1
                    stack[top] = i
edges = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
G = [[0] * 8 for _ in range(8)]
for i in range(0, len(edges), 2):
    G[edges[i]][edges[i+1]] = 1
    G[edges[i+1]][edges[i]] = 1
DFS(1)


# 재귀
edges = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
visited = [0] * 8
G = [[0] * 8 for _ in range(8)]
for i in range(0, len(edges), 2):
   G[edges[i]][edges[i+1]] = 1
   G[edges[i+1]][edges[i]] = 1
def DFSr(v):
   print(v)
   visited[v] = True
   for i in range(1, 8):
       if G[v][i] and not visited[i]:
           DFSr(i)
DFSr(1)