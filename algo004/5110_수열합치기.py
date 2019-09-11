import sys
sys.stdin = open("5110input.txt")

TC = int(input())

for tc in range(1, TC+1):
    n, m = map(int, input().split())
    my_list = [0] * m
    new_list = []
    for i in range(m):
        my_list[i] = list(map(int, input().split()))

    for i in range(1):
        flag = False
        for j in range(n):
            if my_list[i][j] > my_list[i+1][0]:
                flag = True
                if flag:
                    new_list += my_list[i][:j] + my_list[i+1] + my_list[i][j:]
                    break
                else:
                    new_list += my_list[i] + my_list[i+1]

    for x in range(2, m):
        flag = False
        for y in range(len(new_list)):
            if new_list[y] > my_list[x][0]:
                flag = True
                if flag:
                    new_list[y:0] = my_list[x]
                    break
        else:
            new_list.extend(my_list[x])

    s = new_list[-1:-11:-1]
    print('#{}'.format(tc), end=" ")
    for r in s:
        print(r, end=" ")
    print()



