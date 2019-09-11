import sys
sys.stdin = open("2048_input.txt")


TC = int(input())
for tc in range(1, TC+1):
    N, S = input().split()
    N = int(N)
    my_map = [[0] * (N) for _ in range(N)]
    for i in range(N):
        my_map[i] = list(map(int, input().split()))
    print(my_map)

