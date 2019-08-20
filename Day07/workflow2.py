tmp = []
 
def DFSr(v, V):
    # print(v)
    visited[v] = True
    for i in range(1, V+1):
        if G[v][i] and not visited[i]:
            DFSr(i, V)
    tmp.append(v)
     
for test in range(1, 11):
    V, E = list(map(int, input().split()))
    edges = list(map(int, input().split()))
 
    start = []
    end = []
    for i in range(len(edges)):
        if i % 2 == 1:
            end.append(edges[i])
        else:
            start.append(edges[i])
     
    end_point = []
    for i in range(1, V+1):
        if i not in start:
            end_point.append(i)
 
     
    visited = [0] * (V+1)
    G = [[0] * (V+1) for _ in range((V+1))]
 
    for i in range(0, len(edges), 2):
        # 이 문제에서는 거꾸로 가야지 풀린다고 해서 밑의 줄을 주석 처리, 그리고 한쪽 방향으로만 가기 때문에..
        # G[edges[i]][edges[i+1]] = 1
        G[edges[i+1]][edges[i]] = 1
    # print(G)
 
    for i in end_point:
        DFSr(i, V)
 
 
    # print(tmp)
     
 
    answer = '#%d' % test
    for i in tmp:
        answer += ' '
        answer += str(i)
         
    print(answer)
    #1 8 9 4 1 5 2 3 7 6
    tmp = []