import sys
sys.stdin = open("2819_input.txt", "r")


def is_wall(y, x):
    return 0 <= y < 4 and 0 <= x < 4


def move(s, y, x):
    global result
    if len(s) == 7:
        result.add(s)
    else:
        for i in range(4):
            test_y = y + dy[i]
            test_x = x + dx[i]
            if is_wall(test_y, test_x):
                move(s + arr[test_y][test_x], test_y, test_x)


TC = int(input())

for tc in range(1, TC+1):
    arr = [list(input().split()) for i in range(4)]
    result = set()
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    for x in range(4):
        for y in range(4):
            move(arr[y][x], y, x)

    print('#{} {}'.format(tc, len(result)))

