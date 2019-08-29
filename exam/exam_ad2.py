import sys
sys.stdin = open("exam_ad2.txt", "r")

# 상 0 하 1 좌 2 우 3
TC = int(input())
for tc in range(1, TC+1):
    n = int(input())
    atom = [[0] for _ in range(n)]

    for i in range(n):
        atom[i] = list(map(int, input().split()))

    while True:
        for i in range(n):
            if atom[i][2] == 0:
                atom[i][1] -= 1
            elif atom[i][2] == 1:
                atom[i][1] += 1
            elif atom[i][2] == 2:
                atom[i][0] -= 1
            elif atom[i][2] == 3:
                atom[i][0] -= 1



