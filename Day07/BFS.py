def BFS(G, v):  # 그래프 G, 탐색 시작점 v
    visited = [0] * n  # 정점의 개수 n
    queue = []
    queue.append(v)  # 시작점 v를 큐에 삽입
    while queue:  # 큐가 비어있지 않은 경우
        t = queue.pop(0)  # 큐의 첫 번째 원소 반환
        if not visited[t]:  # 방문되지 않은 곳이라면
            visited[t] = True  # 방문한 곳으로 표시
            for i in G[t]:  # t와 연결된 모든 선에 대해
                if not visited[i]:  # 방문되지 않은 곳이라면
                    queue.append(i)  # 큐에 넣기
    return visited


l = [1, 2, 3, 2, 4, 5, 3, 1, 7, 4, 6, 5, 2, 6, 6, 4, 5, 7, 7, 3, 6]
n = 7
print(BFS(l, 1))


