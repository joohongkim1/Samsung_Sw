import sys
sys.stdin = open("input.txt")

for tc in range(10):
    v, e = map(int, input().split())
    edges = list(map(int, input().split()))
    new = set()
    for i in range(0, len(edges), 2):
        new.add(edges[i])
    if 
    # temp = 
    

    # visited = [0] * (v+1)
    # G = [[0] * (v+1) for _ in range(v+1)]
    # for i in range(0, len(edges), 2):
    #     G[edges[i]][edges[i+1]] = 1
    #     G[edges[i+1]][edges[i]] = 1
    # def DFSr(v):
    #     print(v, end=' ')
    #     visited[v] = True
    #     for i in range(1, v+1):
    #         if G[v][i] and not visited[i]:
    #             DFSr(i)
    # DFSr(1)

