s = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

t = int(input())
l = []

for tc in range(1, t+1):
    num, length = input().split()
    case = input().split()
    print('#%d' % tc, end=' ')
    for i in s:
        for j in case:
            if i == j:
                print(i, end=' ')

