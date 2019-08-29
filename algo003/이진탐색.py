import sys
sys.stdin = open("이진탐색input.txt")


def search(start, end, key):
    global count
    count = 0
    while start < end:
        c = int((start + end) / 2)
        if key < c:
            end = c
            count += 1
        elif key > c:
            start = c
            count += 1
        elif c == key:
            count += 1
            break
    return count


TC = int(input())
for tc in range(1, TC + 1):
    p, a, b = map(int, input().split())
    start, end = 1, p
    print('#%d' % tc, end=" ")
    result1 = search(start, end, a)
    result2 = search(start, end, b)

    if result1 < result2:
        print('A')
    elif result1 == result2:
        print('0')
    else:
        print('B')