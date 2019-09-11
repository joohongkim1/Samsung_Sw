import sys
sys.stdin = open("파스칼삼각형_input.txt")


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    l = []
    for _ in range(N):
        l += [[]]
    l[0].append(1)

    for a in range(1, len(l)):
        l[a].append(1)
        for b in range(len(l[a-1]) - 1):
            result = l[a - 1][b] + l[a - 1][b + 1]
            l[a].append(result)
        l[a].append(1)

    print('#{}'.format(tc))
    for x in l:
        temp = ''
        for i in x:
            temp += str(i) + ' '
        print(temp)


