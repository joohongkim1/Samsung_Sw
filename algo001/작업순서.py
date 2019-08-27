import sys
sys.stdin = open("1267input.txt", "r")

TC = 10
for tc in range(1, TC+1):
    my_node, my_line = map(int, input().split())  # 노드수, 간선수
    my_map = [[0]*(my_node+1) for _ in range(my_node+1)]  # 2차원 맵 생성
    # 간선 정보 입력
    data = list(map(int, input().split()))
    n = len(data)//2
    for i in range(n):
        start = data[i*2]  # 짝수 인덱스
        end = data[i*2 + 1]  # 홀수 인덱스
        my_map[end][start] = 1

    result = []  # 작업 경로를 저장
    while True:
        if len(result) == my_node:  # 전체 노드가 경로에 모두 저장되면 종료
            break
        start_col = []
        for col in range(1, my_node+1):  # 모든 칼럼을 검색
            if 1 not in my_map[col] and col not in result:
                start_col.append(col)  # 출발 가능한 노드 등록

        for col in start_col:
            result.append(col)  # 출발 가능 노드를 작업경로에 등록
            for row in range(my_node+1):
                my_map[row][col] = 0  # 출발하는 노드로 연결되는 정보 삭제
    print('#%d' % tc, end=" ")
    for i in result:
        print("%d" % i, end=" ")
    print()

