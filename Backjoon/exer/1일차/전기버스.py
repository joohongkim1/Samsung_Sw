import sys
sys.stdin = open("전기버스_input.txt")


def recur(now):
    global cnt
    while now < N:
        if cnt > N:
            return 0
        elif bus_no[now]:
            now += K
            cnt += 1
        elif not bus_no[now]:
            now -= 1
    return cnt


TC = int(input())
for tc in range(1, TC+1):
    K, N, M = map(int, input().split())
    charge_no = list(map(int, input().split()))
    bus_no = [0] * (N+1)
    cnt = 0

    for i in charge_no:
        bus_no[i] = 1

    print('#{} {}'.format(tc, recur(K)))

