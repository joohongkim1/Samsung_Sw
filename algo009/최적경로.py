import sys
import itertools
sys.stdin = open("최적경로_input.txt", "r")


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    location = list(map(int, input().split()))
    point = []
    min_var = 9999999

    for i in range(4, len(location), 2):
        point.append([location[i], location[i+1]])
    per = list(itertools.permutations(point))

    for x in range(len(per)):
        result_x = abs(location[0] - per[x][0][0]) + abs(per[x][-1][0] - location[2])
        result_y = abs(location[1] - per[x][0][1]) + abs(per[x][-1][1] - location[3])
        for y in range(N-1):
            result_x += abs(per[x][y][0] - per[x][y+1][0])
            result_y += abs(per[x][y][1] - per[x][y+1][1])
            result = result_x + result_y
            if result > min_var:
                break
        else:
            if result < min_var:
                min_var = result

    print('#{} {}'.format(tc, min_var))

    # 일단 백트래킹부터...
    # 간단한 백트래킹해도 안되는거보니까 니 정신나간 itertools땜에 안되는거네
    # 재귀로 ㄱ


    def perm(k):
        if k == r:
            print(t)
        else:
            for i in range(N):
                if visited[i]:
                    continue
                visited[i] = 1
                t[k] = i
                perm(k+1)
                visited[i] = 0

    r = 5
    t = [0] * N
    visited = [0] * N

    perm(0)
