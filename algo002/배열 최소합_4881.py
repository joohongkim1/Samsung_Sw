import sys
sys.stdin = open("4881input.txt")


def find_min(row):  # 단계별로 값을 누적하여 누적 값이 최소값보다 같거나 크면 다음 단계로 안 내려감
    global submin
    for x in range(n):
        if visited[x] == 0:
            visited[x] = 1
            submin += mymap[row][x]  # 최소값 누적변수에 누적
            find_min(row+1)


TC = int(input())
for tc in range(1, TC+1):
    n = int(input())
    mymap = [ list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    mymin = 99999999  # 최소값 저장용
    submin = 0  # 중간 열별 값 저장용, 최소값보다 작으면 최소값에 저장
    find_min(0)
    print('#{} {}'.format(tc, mymin))

