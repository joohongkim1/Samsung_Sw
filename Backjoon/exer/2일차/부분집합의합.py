import sys
sys.stdin = open("부분집합의합_input.txt")


TC = int(input())
A = list(range(1, 13))
for tc in range(1, TC+1):
    N, K = map(int, input().split())
    arr = []
    temp = []
    cnt = 0
    for i in range(1 << 12):
        for j in range(12):
            if i & (1 << j):
                temp.append(A[j])
        arr.append(temp)
        temp = []
    print('#{}'.format(tc), end=' ')
    for j in arr:
        if sum(j) == K and len(j) == N:
            cnt += 1
    print('{}'.format(cnt))