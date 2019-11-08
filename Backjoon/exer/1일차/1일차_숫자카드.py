import sys
sys.stdin = open("숫자카드_input.txt")


TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    card = list(''.join(input()))
    card = sorted(card)
    cnt_arr = [0] * 10
    max_num = 0
    max_idx = 0
    for i in range(len(card)-1, -1, -1):
        cnt_arr[int(card[i])] += 1

    for j in range(len(cnt_arr)-1, -1, -1):
        if max_idx < cnt_arr[j]:
            max_idx = cnt_arr[j]
            max_num = j

    print('#{} {} {}'.format(tc, max_num, max_idx ))