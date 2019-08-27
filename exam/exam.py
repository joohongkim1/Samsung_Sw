'''
[입력]

첫 줄에 총 테스트 케이스의 개수 T가 주어진다.

두 번째 줄부터 T개의 테스트 케이스가 차례대로 주어진다.

각 테스트 케이스의 첫 번째 줄에는 행의 개수 N, 열의 개수 M, 사각형 모양으로 페인트를 칠하는 횟수 K 가 차례대로 주어진다.

이후 K 개의 각 줄에는 페인트를 칠할 사각형의 정보인
 좌측상단 행과 열, 우측하단 행과 열, 페인트의 명도 번호가 차례대로 주어진다.
'''
import sys
sys.stdin = open("exam_input.txt")

TC = int(input())
for tc in range(1, TC+1):
    n, m, k = map(int, input().split())
    my_map = [[0]*m for _ in range(n)]
    info = [[0]*k for _ in range(k)]
    max_var = 0
    cnt = 0
    temp = []
    for i in range(k):
        info[i] = list(map(int, input().split()))

    for i in range(k):
        flag = True
        for x in range(info[i][0], info[i][2]+1):
            if not flag:
                break
            for y in range(info[i][1], info[i][3]+1):
                if my_map[x][y] > info[i][4]:
                    flag = False
                    break
                else:
                    flag = True
        if flag:
            for b in range(info[i][0], info[i][2]+1):
                for c in range(info[i][1], info[i][3]+1):
                    my_map[b][c] = info[i][4]

    for i in range(n):
        for j in range(m):
            temp.append(my_map[i].pop())

    for i in range(n):
        for j in range(0, 11):
            if max_var < temp.count(j):
                max_var = temp.count(j)
    print('#{} {}'.format(tc, max_var))
