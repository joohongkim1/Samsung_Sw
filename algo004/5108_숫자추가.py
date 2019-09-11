import sys
sys.stdin = open("5108input.txt")


TC = int(input())

for tc in range(1, TC+1):
    n, m, l = map(int, input().split())
    sequence = list(map(int, input().split()))

    for i in range(m):
        index, num = map(int, input().split())

        sequence.insert(index, num)

    print('#{} {}'.format(tc, sequence[l]))


