import sys
sys.stdin = open("1961_input.txt")


TC = int(input())
for tc in range(1, TC+1):
    n = int(input())
    my_map = []
    map_90 = []
    map_180 = []
    map_270 = []
    for i in range(n):
        my_map.append(list(map(int, input().split())))
        map_90.append([])
        map_180.append([])
        map_270.append([])

    for j in range(n):
        for i in range(n-1, -1, -1):
            map_90[j].append(my_map[i][j])

    for i in range(n-1, -1, -1):
        for j in range(n-1, -1, -1):
            map_180[n-i-1].append(my_map[i][j])

    for j in range(n-1, -1, -1):
        for i in range(n):
            map_270[n-j-1].append(my_map[i][j])

    print('#{}'.format(tc))
    for i in range(n):
        for j in range(n):
            print('%d' % (map_90[i][j]), end='')
        print(end=' ')
        for jj in range(n):
            print('%d' % (map_180[i][jj]), end='')
        print(end=' ')
        for jjj in range(n):
            print('%d' % (map_270[i][jjj]), end='')
        print()

