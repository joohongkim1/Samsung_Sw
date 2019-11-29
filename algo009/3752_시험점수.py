import sys
sys.stdin = open("3752_input.txt", "r")


TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    point = list(map(int, input().split()))
    n = len(point)
    result = [[] for i in range(1 << n)]
    new = []
    for i in range(0, (1 << n)):
        for j in range(0, n):
            if i & (1 << j):
                result[i].append(point[j])

    result = list(set([tuple(item) for item in result]))

    for i in range(len(result)):
        new.append(sum(result[i]))

    new = set(new)
    print('#{} {}'.format(tc, len(new)))








    # cache = [{} for i in range(N)]
    # visited = [False] * (sum(point) + 1)
    # cnt = 0
    #
    # def my_func(k, temp):
    #     global cnt
    #     if k == N:
    #         if not visited[temp]:
    #             visited[temp] = True
    #             cnt += 1
    #         return
    #
    #     if cache[k].get(temp) == 1:
    #         return
    #
    #     my_func(k+1, temp)
    #     my_func(k+1, temp + point[k])
    #     cache[k][temp] = 1
    #
    # my_func(0,0)
    #
    # print(cnt)

