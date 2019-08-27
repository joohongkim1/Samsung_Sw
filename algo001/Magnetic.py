for tc in range(1, 11):
    n = int(input())
    mymap = []
    for i in range(100):
        row = list(map(int, input().split()))
        mymap.append(row)

        mycount = 0
    for col in range(n):
        meet1 = False
        for row in range(n):
            if mymap[row][col] == 1:
                meet1 = True
            if mymap[row][col] == 2 and meet1 == True:
                mycount += 1
                meet1 = False
    print('#{} {}'.format(tc, mycount))
