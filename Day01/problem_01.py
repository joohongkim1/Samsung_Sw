# min max

t = int(input())

for i in range(1, t+1):
    N = int(input())
    x = list(map(int, input().split()))
    for a in range(N-1, 0, -1):
        for b in range(0, a):
            if x[b] > x[b+1]:
                x[b], x[b+1] = x[b+1], x[b]
    print('#%d %d' % (i, x[-1] - x[0]))


# 강사님

# def find(a, n):

#     max_value = a[0]
#     min_value = a[0]

#     for i in range(1, n):
#         if a[i] > max_value:
#             max_value = a[i]
#         if a[i] < min_value:
#             min_value = a[i]

#     return max_value - min_value

# T = int(input())

# for i in range(1, T+1):
#     n = int(input())
#     a = list(map(int, input().split()))
#     print(find(a, n))