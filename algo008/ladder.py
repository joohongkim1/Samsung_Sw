import sys
sys.stdin = open("ladder.txt")


def isWall(y, x):
    return 0 <= y < 100 and 0 <= x < 100 and ladder[y][x]

def move(y, x):
    pass


for tc in range(1, 11):
    test_case = int(input())
    ladder = [[0] * 100 for _ in range(100)]
    for i in range(100):
        ladder[i] = list(map(int, input().split()))

    for y in range(100):
        for x in range(100):
            if ladder[y][x] == 2:
                startY = y
                startX = x
                break

