'''
3
4
1 3 2 1
6
2 1 1 2 3 3
7
1 3 3 3 1 1 3
'''
# 인원수가 1명, 2명, 4명일 경우는 어떻게?

import sys
sys.stdin = open("4880input.txt")


TC = int(input())
for tc in range(1, TC+1):
    n = int(input())
    card = input().split()
    left_side = len(card) // 2
    right_side = len(card) // 2 + 1
    print(left_side, right_side)