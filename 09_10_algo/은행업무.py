import sys
sys.stdin = open("은행업무_input.txt")

from copy import deepcopy
TC = int(input())

for tc in range(1, TC+1):
    bin1 = list(map(int, input()))
    ter = list(map(int, input()))
    temp = deepcopy(bin1)
    temp2 = deepcopy(ter)
    result = 0
    result2 = 0

    print('#%s' % tc, end=' ')
    for i in range(len(bin1)):
        bin1 = deepcopy(temp)
        result = 0
        if bin1[i] == 0:
            bin1[i] = 1
        else:
            bin1[i] = 0
        for j in range(len(bin1)-1, -1, -1):
            result += bin1[j] * pow(2, len(bin1)-j-1)

        for i in range(len(ter)):
            ter = deepcopy(temp2)
            result2 = 0
            if ter[i] == 0:
                ter[i] = 1
            elif ter[i] == 1:
                ter[i] = 0
            else:
                ter[i] = 0
            for j in range(len(ter)-1, -1, -1):
                result2 += ter[j] * pow(3, len(ter)-j-1)
            if result == result2:
                print('%d' % result2)
                break

        for i in range(len(ter)):
            ter = deepcopy(temp2)
            result2 = 0
            if ter[i] == 0:
                ter[i] = 2
            elif ter[i] == 1:
                ter[i] = 2
            else:
                ter[i] = 1
            for j in range(len(ter)-1, -1, -1):
                result2 += ter[j] * pow(3, len(ter)-j-1)
            if result == result2:
                print('%d' % result2)
                break

