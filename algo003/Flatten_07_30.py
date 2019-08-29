import sys
sys.stdin = open("flatten_input.txt")


for tc in range(1, 11):
    dump = int(input())
    height = list(map(int, input().split()))

    for i in range(dump):
        height[height.index(min(height))] += 1
        height[height.index(max(height))] -= 1
    print('#{} {}'.format(tc, max(height) - min(height)))


