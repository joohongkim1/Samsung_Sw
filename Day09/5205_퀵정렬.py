import sys
sys.stdin = open("5205_input.txt", "r")


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
    return quick_sort(lesser_arr) + [pivot] + quick_sort(greater_arr)

TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    arr = list(map(int, input().split()))
    A = []
    A += quick_sort(arr)
    print(A)

    print('#{} {}'.format(tc, A[N//2]))



