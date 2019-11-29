'''
1. 1일 이용권 사용시 cost에 해당 월 (now) 이용 날짜 * 1일 이용권 사용비용을 더해주고
 위치를 1 더한다.

2. 1달 이용권 사용시 cost에 1달 이용권 사용비용을 더해주고 위치를 1 더한다.

3. 3달 이용권 사용시 cost에 3달 이용권 사용비용을 더해주고 위치를 3 더한다.



now가 12 이상이 되면 ans과 비교를 통해 현재 cost가 더 작으면 갱신하고 함수를 종료한다.
'''

import sys
sys.stdin = open("수영장_input.txt", "r")


def a(now, cost):
    global ans
    if now >= 12:
        if cost < ans:
            ans = cost
        return
    a(now+1, cost+charge[0]*plan[now])
    a(now+1, cost+charge[1])
    a(now+3, cost+charge[2])


TC = int(input())
for tc in range(1, TC+1):
    charge = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    ans = charge[3]
    a(0, 0)
    print('#{} {}'.format(tc, ans))
