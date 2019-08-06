T = int(input())

for case in range(1, T+1):
    start = 1
    p, pa, pb = map(int, input().split())
    c = 0
    cntA = 0
    cntB = 0
    temp_p = p

    while start < p:
        cntA += 1
        c = int((start + p) / 2)
        if pa > c:
            start = c
        elif pa < c:
            p = c
        else:
            break

    start = 1
    while start < temp_p:
        cntB += 1
        c = int((start + temp_p) / 2)
        if pb > c:
            start = c
        elif pb < c:
            temp_p = c
        else:
            break
        
    if cntA > cntB:
        print('#%d B' % case)
    elif cntA < cntB:
        print('#%d A' % case)
    else:
        print('#%d 0' % case)

    