import sys
sys.stdin = open("이진수2_input.txt", "r")


TC = int(input())
for tc in range(1, TC+1):
    n = float(input())
    temp = []
    while n != 0.0:
        n *= 2
        if n >= 1:
            n -= 1
            temp.append(1)
        else:
            temp.append(0)

    print('#{}'.format(tc), end=' ')
    if len(temp) >= 13:
        print('overflow')
    else:
        for i in temp:
            print(i, end='')
        print()






