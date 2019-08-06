T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charging_st = list(map(int, input().split()))
    stations = [0] * (N + 1)
    for i in range(M):
        stations[charging_st[i]] = 1

    cnt = cur = 0
    while(True):
        pre = curcur += K 