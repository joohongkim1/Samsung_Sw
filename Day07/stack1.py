import sys
sys.stdin = open("sample_input.txt")

t = int(input())

for tc in range(1, t+1):
    v, e = map(int, input().split())
