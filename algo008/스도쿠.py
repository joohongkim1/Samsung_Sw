TC = int(input())

for tc in range(1, TC+1):
    my_map = [[0] * 9 for _ in range(9)]

    for i in range(9):
        my_map[i] = list(map(int, input().split()))

    print(my_map)