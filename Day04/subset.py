T = int(input())
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
n = len(A)
my_list = []


for i in range(1<<n):
        subset = []
        for j in range(n):
            if i & (1<<j):
                subset.append(A[j])
        my_list.append(subset)
    
for case in range(1, T+1):
    N, K = map(int, input().split())
    count = 0

    for i in range(len(my_list)):
        sum = 0
        cnt = 0
        for j in range(len(my_list[i])):
            sum += my_list[i][j]
            cnt += 1
        if sum == K and cnt == N:
            count += 1
    
    print('#%d' % case, count)


        

