'''
다음 100X100의 2차원 배열이 주어질 때, 
각 행의 합, 각 열의 합, 각 대각선의 합 중 
최댓값을 구하는 프로그램을 작성하여라.
다음과 같은 5X5 배열에서 최댓값은 29이다.

총 10개의 테스트 케이스가 주어진다.
배열의 크기는 100X100으로 동일하다.
각 행의 합은 integer 범위를 넘어가지 않는다.
동일한 최댓값이 있을 경우, 하나의 값만 출력한다.

각 테스트 케이스의 첫 줄에는 테스트 케이스 번호가 주어지고 그 다음 줄부터는 
2차원 배열의 각 행 값이 주어진다.
'''

for case in range(1, 11):
    test_num = int(input())
    n, m = 100, 100
    arr = [0] * n
    max_value = 0

    for i in range(n):
        arr[i] = list(map(int, input().split()))

    for x in range(n):
        sum1 = 0
        sum2 = 0
        
        for y in range(m):
            sum1 += arr[x][y]
            sum2 += arr[y][x]
            if max_value < sum1:
                max_value = sum1
            elif max_value < sum2:
                max_value = sum2


    for x in range(n):
        sum4 = 0
        for y in range(m-1, -1, -1):
            sum4 += arr[x][y]
            if max_value < sum4:
                max_value = sum4
                
    sum3 = 0
    for x in range(n):
        sum3 += arr[x][x] 
        if max_value < sum3:
            max_value = sum3                
    print(f'#{case} {max_value}')


                