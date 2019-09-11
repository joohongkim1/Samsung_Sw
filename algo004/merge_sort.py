l = [69, 10, 30, 2, 16, 8, 31, 22]


def merge_sort(m):
    if len(m) <= 1:
        return m

    # 1. Divide
    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]

    # 리스트 크기 1 될 때까지 재귀호출
    left = merge_sort(left)
    right = merge_sort(right)

    # 2. CONQUER 부분 : 분할 리스트를 병합

    return merge(left, right)


def merge(left, right):
    result = []

    while len(left) > 0 and len(right) > 0:  # 양 리스트에 원소가 남은 경우
        # 두 서브 리스트의 첫 원소를 비교하여 작은 것부터 result 에 추가
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if len(left) > 0:
        result.extend(left)
    if len(right) > 0:
        result.extend(right)
    return result


print(merge_sort(l))