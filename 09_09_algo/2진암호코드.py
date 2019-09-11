import sys
sys.stdin = open("암호코드_input.txt")


TC = int(input())

for tc in range(1, TC+1):
    n, m = map(int, input().split())
    my_map = []
    a = []
    b = []
    even = odd = 0
    for i in range(n):
        my_map.append(list(map(str, input().split())))

    data = ["0001101", "0011001", "0010011", "0111101", "0100011",
            "0110001", "0101111", "0111011", "0110111", "0001011",]

    for i in range(n):
        if '1' in my_map[i][0]:
            a.append(my_map[i][0])
            break

    for i in range(m-1, -1, -1):
        if a[0][i] == '1':
            a.append(a[0][i:i-56:-1])
            break
    a = [a[1][::-1]]

    for i in range(0, len(a[0]), 7):
        a.append(a[0][i:i+7])
    for i in range(1, 9):
        for j in range(len(data)):
            if a[i] == data[j]:
                b.append(j)
                break
    for i in range(8):
        if i % 2 == 0:
            odd += b[i]
        else:
            even += b[i]

    result = odd * 3 + even
    print('#%d' % tc, end=' ')
    if result % 10 == 0:
        print(sum(b))
    else:
        print('0')
