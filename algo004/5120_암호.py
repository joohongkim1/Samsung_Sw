import sys
sys.stdin = open("5120input.txt")


TC = int(input())

for tc in range(1, TC+1):
    n, m, k = map(int, input().split())
    num = list(map(int, input().split()))
