import sys
sys.stdin = open("상금_input.txt", "r")


TC = int(input())

for tc in range(1, TC+1):
    num, swap = list(input().split())
    arr = []
    max_var = 0
    max_idx = 0
    for i in range(len(num)):
        arr.append(num[i])









