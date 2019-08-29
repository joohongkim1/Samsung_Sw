'''
3
4
1 3 2 1
6
2 1 1 2 3 3
7
1 3 3 3 1 1 3
'''
import sys
sys.stdin = open("4880input.txt")


def battle(card_no1, card_no2):
    if data[card_no1] == data[card_no2]:  # 카드 번호가 작으면 승
        if card_no1 < card_no2:
            return card_no1
        return card_no2
    if data[card_no1] == "1":
        if data[card_no2] == "2":
            return card_no2
        else:
            return card_no1

    if data[card_no1] == "2":
        if data[card_no2] == "3":
            return card_no2
        else:
            return card_no1

    if data[card_no1] == "3":
        if data[card_no2] == "1":
            return card_no2
        else:
            return card_no1


def mydiv(start, end):
    # 종료
    if start == end:  # 한 장으로 나눠진 경우
        return start
    p = (start + end) // 2  # 반 나누는 기준 번호
    card_no1 = mydiv(start, p)  # 한 장까지 분할, 카드의 번호 반환
    card_no2 = mydiv(p+1, end)  # 한 장까지 분할, 카드의 번호 반환
    winner_card_no = battle(card_no1, card_no2)
    return winner_card_no # 승자 카드 번호 반환


TC = int(input())
for tc in range(1, TC+1):
    n = int(input())
    data = list(map(int, input().split()))
    winner = mydiv(0, n-1)

    print('#{} {}'.format(tc, winner+1))