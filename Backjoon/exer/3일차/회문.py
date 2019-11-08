import sys
sys.stdin = open("회문.txt")


TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    arr = [''] * N
    for n in range(N):
        arr[n] = list(input())
    # print('#{}'.format(tc), end=' ')
    # for i in range(N):
    #     for j in range(N-M+1):
    #         if arr[i][j:j+M] == list(reversed(arr[i][j:j+M])):
    #             print(''.join(arr[i][j:j+M]))


