import sys
sys.stdin = open("4881input.txt")


t = int(input())

for tc in range(1, t+1):
    n = int(input())
    num = [[0]*n for _ in range(n)]
    sum = 0
    min_var = max(num)
    for i in range(n):
        num[i] = list(map(int, input().split()))

