import sys
sys.stdin = open("문자열.txt")


def search(str1, str2):
    now = 0
    target = 0
    flag = True
    while now <= len(str1) - 1 and target <= len(str2) - 1:
        if str1[now] == str2[target]:
            flag = True
            now += 1
            target += 1
        else:
            flag = False
            target += 1

    if flag:
        return 1
    return 0


TC = int(input())
for tc in range(1, TC+1):
    str1 = list(input())
    str2 = list(input())
    print('#{}'.format(tc), end=' ')
    print(search(str1, str2))

