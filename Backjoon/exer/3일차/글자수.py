import sys
sys.stdin = open("글자수.txt")


TC = int(input())
for tc in range(1, TC+1):
    str1 = list(input())
    str2 = list(input())
    cnt = [0] * (len(str1))

    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                cnt[i] += 1

    print('#{} {}'.format(tc, max(cnt)))



