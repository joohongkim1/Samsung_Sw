import sys
sys.stdin = open("회전_input.txt")

TC = int(input())

for tc in range(1, TC+1):
    n, m = map(int, input().split())
    x = list(map(int, input().split()))

    for i in range(m):
        x.append(x[0])
        x.pop(0)

    print('#{} {}'.format(tc, x[0]))