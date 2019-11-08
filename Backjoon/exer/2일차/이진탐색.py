import sys
sys.stdin = open("이진탐색.txt")


def search(start, end, target):
    cnt = 0
    while start <= end:
        cnt += 1
        middle = int((start + end) / 2)

        if middle < target:
            start = middle
        elif middle > target:
            end = middle
        else:
            return cnt


TC = int(input())
for tc in range(1, TC+1):
    P, Pa, Pb = map(int, input().split())

    print('#{}'.format(tc), end=' ')
    if search(1, P, Pa) < search(1, P, Pb):
        print('{}'.format('A'))
    elif search(1, P, Pa) > search(1, P, Pb):
        print('{}'.format('B'))
    else:
        print('{}'.format(0))
