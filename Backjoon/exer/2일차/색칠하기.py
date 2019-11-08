import sys
sys.stdin = open("색칠하기.txt")


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [0] * N
    color_1 = []
    color_2 = []
    for n in range(N):
        arr[n] = list(map(int, input().split()))

