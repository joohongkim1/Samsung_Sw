'''
첫 줄에 테스트 케이스 개수 T가 주어진다.   ( 1 ≤ T ≤ 50 )

다음 줄부터 테스트케이스의 첫 줄에 칠할 영역의 개수 N이 주어진다. ( 2 ≤ N ≤ 30 )

다음 줄에 왼쪽 위 모서리 인덱스 r1, c1, 오른쪽 아래 모서리 r2, c2와 색상 정보 color가 주어진다. ( 0 ≤ r1, c1, r2, c2 ≤ 9 )

color = 1 (빨강), color = 2 (파랑)
'''
T = int(input())

for case in range(1, T + 1):
    n = int(input())
    my_list = []
    count = 0
    for i in range(n):
        r1, c1, r2, c2, color = map(int, input().split())

        for x in range(r1, r2 + 1):
            for y in range(c1, c2 + 1):
                my_list.append([x, y])

    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            if my_list[i] == my_list[j]:
                count += 1

    print('#%d' % case, count)