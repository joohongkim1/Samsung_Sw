T = int(input())

for case in range(1, T+1):
    n = int(input())
    my_list = []
    count = 0 
    for i in range(n):
        r1, c1, r2, c2, color = map(int, input().split())

        for x in range(r1, r2+1):
            for y in range(c1, c2+1):
                my_list.append([x, y])

    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)):
            if my_list[i] == my_list[j]:
                count += 1
    
    print('#%d' % case, count)


