import sys
sys.stdin = open("이진수_input.txt")

TC = int(input())

for tc in range(1, TC+1):
    n, hex_d = input().split()
    l = []

    scale = 16
    length = len(hex_d) * 4
    hex_to_bin = bin(int(hex_d))[2:].zfill(bits)
    # zero_count = length - len(hex_to_bin)
    # print('#{}'.format(tc), end = ' ')
    # for i in range(zero_count):
    #     print(0, end='')
    # print(hex_to_bin)
