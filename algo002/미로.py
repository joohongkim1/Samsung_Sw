'''
NxN 크기의 미로에서 출발지에서 목적지에 도착하는 경로가 존재하는지 확인하는 프로그램을 작성하시오.
도착할 수 있으면 1, 아니면 0을 출력한다. 주어진 미로 밖으로는 나갈 수 없다.
다음은 5x5 미로의 예이다.
13101
10101
10101
10101
10021
마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 도착할 수 있는지 확인하면 된다.
[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄부터 테스트 케이스의 별로 미로의 크기 N과 N개의 줄에 걸쳐 미로의 통로와 벽에 대한 정보가 주어진다.
0은 통로, 1은 벽, 2는 출발, 3은 도착이다. 5<=N<=100
[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 계산결과를 정수로 출력하거나 또는 ‘error’를 출력한다.
'''

import sys
sys.stdin = open("4875input.txt", "r")


def is_ok(y, x):  # 해당 좌표가 이동가능한지 여부 확인 함수
    return 0 <= y < n and 0 <= x < n and mymap[y][x] != 1


def find_map(startY, startX):  # 재귀함수
    # 1. 종료조건
    global result
    if mymap[startY][startX] == 3:
        result = 1
        return # 검색 종료

    # 2. 반복검색
    # 4방향 검색

    visited.append((startY, startX))
    if result == 0 and is_ok(startY, startX+1) and (startY, startX+1) not in visited:
        find_map(startY, startX+1)  # 우측
    if result == 0 and is_ok(startY+1, startX) and (startY+1, startX) not in visited:
        find_map(startY+1, startX)  # 아래
    if result == 0 and is_ok(startY, startX-1) and (startY, startX-1) not in visited:
        find_map(startY, startX-1)  # 왼쪽
    if result == 0 and is_ok(startY-1, startX) and (startY-1, startX) not in visited:
        find_map(startY-1, startX)  # 위


TC = int(input())

for tc in range(1, TC+1):
    n = int(input())  # 한 변의 길이
    mymap = []  # 지도 정보
    for i in range(n):
        l = list(input())
        mymap.append(l)

    # 시작 지점 찾기
    startX = -1
    startY = -1
    for y in range(n):
        for x in range(n):
            if mymap[y][x] == 2:
                startX, startY = x, y
    # 미로 문제 풀 때 -> 방문했던 위치 저장소가 반드시 필요
    visited = []
    result = 0  # 목적지 도착 여부
    find_map(startY, startX)
    print('#{} {}'.format(tc, result))
