import sys
sys.stdin = open("4869input.txt","r")


def paper(w):
    if w == n : # 목표 너비가 되면
        return 1
    elif w > n : # 목표 너비보다 크면
        return 0
    return paper(w+10) + paper(w+20)*2


tc= int(input())
for tc in range(1, tc+1):
    n = int(input()) # 목표 너비
    r = paper(0)
    print("#{} {}".format(tc, r))