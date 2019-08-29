import sys
sys.stdin = open("GNS_input.txt")


TC = int(input())
num_str = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

for tc in range(1, TC+1):
    case, length = input().split()
    num = input().split()
    l = []
    print(case)
    for i in range(len(num_str)):
        for j in range(len(num)):
            if num_str[i] == num[j]:
                l.append(num[j])

    for i in l:
        print(i, end=' ')
    print()
