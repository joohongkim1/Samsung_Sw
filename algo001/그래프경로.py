import sys
sys.stdin = open("4871input.txt", "r")


def search_map(start):  # 행 번호
    global result
    visited[start] = 1  # 방문한 곳은 1
    for next in range(1, my_node+1):
        if my_map[start][next] == 1 and not visited[next]:  # 안 가본 곳
            if next == end:
                result = 1  # 갈 수 있는 곳
                return
            search_map(next)  # 다음 노드로 가서 검색


TC = int(input())
for tc in range(1, TC+1):
    my_node, my_line = map(int, input().split())
    my_map = [[0]*(my_node+1) for _ in range(my_node+1)]
    visited = [0]*(my_node+1)  # 방문했던 곳 표시

    for i in range(my_line):  # 간선의 갯수만큼 읽기
        start, end = map(int, input().split())
        my_map[start][end] = 1

    start, end = map(int, input().split())
    result = 0  # 갈 수 있으면 1 없으면 0
    search_map(start)

    print('#{} {}'.format(tc, result))
