import sys
sys.stdin = open("view_input.txt")


for tc in range(1, 11):
    length = int(input())
    case = list(map(int, input().split()))
    count = 0

    for i in range(2, len(case)-2):
        if case[i-1] < case[i] and case[i-2] < case[i] and case[i] > case[i+1] and case[i] > case[i+2]:
            count += case[i] - max(case[i - 1], case[i - 2], case[i + 1], case[i + 2])
    print('#{} {}'.format(tc, count))



