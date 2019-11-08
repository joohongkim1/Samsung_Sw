import sys
sys.stdin = open("카드게임.txt")


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    card = list(map(int, input().split()))


